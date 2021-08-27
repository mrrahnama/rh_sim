import copy
import csv
import datetime
import pickle
import random

import dill as dill
from mesa.datacollection import DataCollector
from mesa.model import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from numpy import random

from agents import Customer, Seller, Negotiation,Product

default_range_product_costs =3000000
default_number_product = 50
default_min_price=700000


class Market(Model):
    def __init__(self, width=20, height=20, report_address="",max_steps=1000,customerTypes = None,sellers=None,hasgrid=True):
        Model.__init__(self)
        # super().__init__(self,seed=seed)
        self.product_list={}
        self.customers=[]
        self.sellers = {}
        self.running=True
        self.customerTypes=[]
        self.customerTypesDic={}
        self.number_of_customer = 0
        self.number_of_seller=0
        if hasgrid:
            self.grid = MultiGrid(width, height, False)
        else:
            self.grid = None
        self.schedule = RandomActivation(self)
        self.report_address=report_address
        self.step_report=[]
        if isinstance(sellers,int):
            self.number_of_seller = sellers
            self.create_sellers()
        elif isinstance(sellers,dict):
            self.number_of_seller=len(sellers)
            i=1
            for key,val in sellers.items():
                if isinstance(val, Seller):
                    val.model = self
                    val.unique_id=i
                    sellers[key]=val
                    i=i+1
            self.sellers = sellers
            self.addsellerGrid()
        if customerTypes is not None:
            for typename,typ in customerTypes.items():
                if isinstance(typ,Customer):
                    c=CustomerType(samplecustomer=typ,typeName=typ.type_name,lambdafile="lambda.csv",contprobfile="contprob.csv")
                    c.setlambda()
                    c.setcontprob()
                    self.customerTypesDic[typ.type_name] = c
                else:
                    c=typ
                    self.customerTypesDic[typ.typeName] = c

        self.transactions =[]
        self.failed_transactions=[]
        self.max_steps=max_steps
        self.model_data={}
        self.setmodeldatareport()
        # data = {"Customer": lambda m: m.number_of_customer,
        #         "Seller": lambda m: m.number_of_seller,
        #         }
        # data2 = {"s1": lambda m: m.revenue,
        # "s2": lambda m: m.revenue,
        # }
        # "transaction":lambda m: m.transactions,
        # "faild_transaction" :lambda m: m.failed_transactions,
        # agent_data={"Wealth": lambda x: x.wealth}
        self.datacollector = DataCollector(self.model_data)
        self.datacollector.collect(self)
        self.generateCustomers()
    def setmodeldatareport(self):
        self.model_data = {
            "Customer": lambda m: len(m.customers),
            "Seller": lambda m: m.number_of_seller}
    def collectStepReport(self):
        self.step_report.append({"seller_"+str(seller.unique_id) : seller.revenue - seller.laststepinffo['revenue'] for seller in self.sellers.values()})
        if self.running is False:
            current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            with open(self.report_address + current_time + 'r_step_report.csv', 'w', newline='') as f:
                # fieldnames lists the headers for the csv.
                w = csv.DictWriter(f, fieldnames=self.step_report[0].keys())
                w.writeheader()
                for obj in self.step_report:
                    # Build a dictionary of the member names and values...
                    w.writerow(obj)
            with open(self.report_address + current_time + 'r_seller_offerlists.csv', 'w', newline='') as f:
                # fieldnames lists the headers for the csv.
                w = csv.DictWriter(f, fieldnames=self.sellers.keys())
                w.writeheader()
                # Build a dictionary of the member names and values...
                for i in range(len(list(self.sellers.values())[0].inventory)):
                    w.writerow({seller.unique_id:list(seller.inventory.keys())[i] for seller in self.sellers.values()})
    def step(self):
        print(" step:" + str(self.schedule.steps) )
        # if not(self.grid.exists_empty_cells()):
        if  self.schedule.steps > self.max_steps:
            self.running = False
            # br_step_data = pd.DataFrame()
            # self.datacollector.get_model_vars_dataframe()
            # br_step_data.append(
            current_time=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            with open(self.report_address+current_time+'r_detailed_transaction.csv','w',newline='') as f:
            # fieldnames lists the headers for the csv.
                w = csv.DictWriter(f, fieldnames=vars(Negotiation(0, 0, 0, 0, 0, 0, 0)))
                w.writeheader()
                for obj in self.transactions:
            # Build a dictionary of the member names and values...
                    w.writerow({k:getattr(obj,k) for k in vars(self.transactions[0])})
            # br_step_data.to_csv("market_Step_Data.csv")
            with open(self.report_address+current_time+"r_sellers.csv",'w',newline='') as f:
            # fieldnames lists the headers for the csv.
                field_names=['unique_id','name','failed_transaction','succesful_transaction','revenue','profit', 'inventory_count']
                w = csv.DictWriter(f,fieldnames= field_names)
                w.writeheader()
                for seller in self.sellers.values():
                    seller.inventory_available()
            # Build a dictionary of the member names and values...
                    w.writerow({k:getattr(seller,k) for k in field_names})
            self.collectStepReport()
            return

        self.schedule.step()
        self.datacollector.collect(self)
        self.collectStepReport()

        for seller in self.sellers.values():
            seller.revenuebystep.append(seller.revenue-seller.laststepinffo['revenue'])
            seller.laststepinffo['revenue']=seller.revenue
        self.generateCustomers()
    def generateCustomers(self):
        self.customers=[]
        #for cusType in self.customerTypes:
        for cusType in self.customerTypesDic.values():
            startid=len(self.customers)
            # print(" step:" +str( self.schedule.steps)+ "     ctyp: " +cusType.typeName +"")
            self.customers.extend(self.create_customer_custype(cusType, startid))
        self.addCusGrid()
        self.addCusSch()
    def create_customer_custype(self, customerType, id):
        if isinstance(customerType, CustomerType):  #TODO:  change  type to customerType 
            uid = id
            customer_generated = []
            ll=customerType.getLambda(self.schedule.steps)
            if ll<0:
                ll=0
            populationSize = int(random.poisson(lam=ll))
            for i in range(populationSize):
                new_customer = Customer(uid, self)
                new_customer.lifetime = customerType.sampleCustomer.lifetime
                new_customer.preference_list = customerType.sampleCustomer.preference_list
                new_customer.seller_preferencelist = customerType.sampleCustomer.seller_preferencelist
                new_customer.type_name = customerType.typeName
                customer_generated.append(new_customer)
                uid = uid + 1
            return customer_generated
    def addCusSch(self):
        for new_customer in self.customers:
            self.schedule.add(new_customer)
    def addCusGrid(self):
        for new_customer in self.customers:
            self.grid.place_agent(new_customer,self.grid.find_empty())
    def addsellerGrid(self):
        for seller in self.sellers.values():
            self.grid.place_agent(seller,self.grid.find_empty())
    # def create_customers(self,customerTypes=None):
    #     if isinstance(customerTypes,dict):
    #         uid =1
    #         customer_generated=0
    #         for customer_type in customerTypes:
    #                 type_customer = copy.copy(customerTypes[customer_type])
    #                 new_customer = Customer(uid, self)
    #                 new_customer.lifetime=type_customer.lifetime
    #                 new_customer.preference_list=type_customer.preference_list
    #                 new_customer.seller_preferencelist=type_customer.seller_preferencelist
    #                 new_customer.type_name=type_customer.type_name
    #                 self.grid.place_agent(new_customer,self.grid.find_empty())
    #                 self.schedule.add(new_customer)
    #                 self.customers.append(new_customer)
    #                 uid =uid + 1
    #                 customer_generated=1+customer_generated
    #         self.number_of_customer = customer_generated
    #     else:
    #         for i in range(self.number_of_customer):
    #             new_customer = Customer(i, self)
    #             self.grid.place_agent(new_customer,self.grid.find_empty())
    #             self.schedule.add(new_customer)
    #             self.customers.append(new_customer)
    def create_sellers(self):
        self.sellers = {}
        for i in range(self.number_of_seller):
            new_seller = Seller(i, self)
            if self.grid is not None:
                self.grid.place_agent(new_seller,self.grid.find_empty())
            # self.schedule.add(new_seller)
            self.sellers[i]=new_seller
    def gen_rand_productlist(self,**kwarg):
        if "price_interval" in kwarg.keys():
            price_interval= kwarg["price_interval"]
        else:
            price_interval = default_range_product_costs
        if "number" in kwarg.keys():
            number= kwarg["number"]
        else:
            number=default_number_product
        if "min_price" in kwarg.keys():
            min_price= kwarg["min_price"]
        else:
            min_price= default_min_price
        for i in range(number):
            self.product_list[i]= round(random.random(),2) *price_interval+min_price
    def gen_usercsv_productlist(self,**kwarg):
        # df = pd.read_csv(kwarg['file_path'])
        # df_temp = df.iloc[:,0:2]
        # df.values.tolist()
        with open(kwarg['file_path']) as f:
            reader = csv.reader(f)
            for row in reader:
                self.product_list[row[0]]=row[1]
    def poissonLamGen(self):
        pass

class CustomerType:
    def __init__(self, samplecustomer=None,typeName="",  lambdafile="", contprobfile=""):
        if  isinstance(samplecustomer,Customer):
            self.sampleCustomer=samplecustomer
        self.lambdaArray = []
        self.contprobArray=[]
        self.typeName=typeName
        self.lambdafile=lambdafile
        self.contprobfile=contprobfile
        self.lambdafixval=None
        self.contprobfixval=None

    def setlambda(self, filepath=""):
        if filepath=="":
            filepath=self.lambdafile
        with open(filepath, newline='') as csvfile:
            self.lambdaArray = list(csv.reader(csvfile,quoting=csv.QUOTE_NONNUMERIC))[0]

    def getLambda(self, currentStep):
        return self.lambdaArray[currentStep]

    def setcontprob(self, filepath=""):
        if filepath=="":
            filepath=self.contprobfile
        with open(filepath, newline='') as csvfile:
            self.contprobArray = list(csv.reader(csvfile,quoting=csv.QUOTE_NONNUMERIC))[0]

    def getcontprob(self, tryNo):
        return self.contprobArray[tryNo-1]

            

if __name__ == "__main__":
    market1 = Market()
    s = Seller(5,market1, "seller1")
    with open("sellerTypes\\seller_type_" + s.name + '.txt', 'wb') as file1:
        pickle.dump(s, file1)
    print(random.randn())
    m=CustomerType(lambdafile="lambda.csv",contprobfile='contprob.csv')
    m.setlambda()
    m.setcontprob()
    print(m.getcontprob(4))
    # c1= Customer(1,market1) 
    # # market1.gen_rand_productlist(min_price=100000,price_interval=300000,number=50)
    # market1.gen_usercsv_productlist(file_path="file.csv")
    # print(market1.product_list)
    # # for i in range(10):
        # c1.step()
        # s1=Seller(i,market1)

