import random
from mesa.model import Model
from mesa.space import SingleGrid,MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from agents import Customer,Seller ,negotiation
import pandas as pd
import csv ,copy
import datetime
default_range_product_costs =3000000
default_number_product = 50
default_min_price=700000


class Market(Model):
    def __init__(self, width=20, height=20, num_customer=50,num_seller=4,report_address="",max_steps=1000,customerTypes = None):
        Model.__init__(self)
        # super().__init__(self,seed=seed)
        self.number_of_customer = num_customer
        self.number_of_seller = num_seller
        self.grid = MultiGrid(width, height, False)
        self.schedule = RandomActivation(self)
        self.report_address=report_address
        self.running=True
        self.product_list={}
        self.customers=[]
        self.sellers =[]
        # if sellerTypes == {}:
        self.create_sellers()
        # else:
        #     self.create_sellers()
        if customerTypes == None:
            self.create_customers()
        else:
            self.customerTypes= customerTypes
            self.create_customers(self.customerTypes)
        self.transactions =[]
        self.failed_transactions=[]
        self.max_steps=max_steps
        model_data={        
                "Customer": lambda m: m.number_of_customer,
                "Seller": lambda m: m.number_of_seller,
        }
        # data = {"Customer": lambda m: m.number_of_customer,
        #         "Seller": lambda m: m.number_of_seller,
        #         }
        # data2 = {"s1": lambda m: m.revenue,
        # "s2": lambda m: m.revenue,
        # }
        # "transaction":lambda m: m.transactions,
                # "faild_transaction" :lambda m: m.failed_transactions,
        # agent_data={"Wealth": lambda x: x.wealth}
        self.datacollector = DataCollector(model_data)
        self.datacollector.collect(self)
    def step(self):
        self.generateCustomer()
        self.schedule.step()
        self.datacollector.collect(self)
        # if not(self.grid.exists_empty_cells()):
        if self.number_of_customer == 0 or self.schedule.steps>self.max_steps:
            self.running = False
            # br_step_data = pd.DataFrame()
            # self.datacollector.get_model_vars_dataframe()
            # br_step_data.append(
            current_time=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            with open(self.report_address+current_time+'r_detailed_transaction.csv','w',newline='') as f:
            # fieldnames lists the headers for the csv.
                w = csv.DictWriter(f,fieldnames=vars(negotiation(0,0,0,0,0,0)))
                w.writeheader()
                for obj in self.transactions:
            # Build a dictionary of the member names and values...
                    w.writerow({k:getattr(obj,k) for k in vars(self.transactions[0])})
            # br_step_data.to_csv("market_Step_Data.csv")
            with open(self.report_address+current_time+"r_sellers.csv",'w',newline='') as f:
            # fieldnames lists the headers for the csv.
                field_names=['unique_id','failed_transaction','succesful_transaction','revenue','profit','inventory_count']
                w = csv.DictWriter(f,fieldnames=field_names)
                w.writeheader()
                for seller in self.sellers:
                    seller.inventory_available()
            # Build a dictionary of the member names and values...
                    w.writerow({k:getattr(seller,k) for k in field_names})
    def generateCustomer(self):
        for cusType in self.customerTypes:
            pass
            
    def create_custpomers(self, customerTypes= None,poisson=""):
        pass
    def create_customers(self,customerTypes=None):
        if isinstance(customerTypes,dict):
            uid=1
            customer_generated=0
            for customer_type in customerTypes:
                for i in range(int(self.number_of_customer*customerTypes[customer_type].percentofall/100)):
                    type_customer = copy.copy(customerTypes[customer_type])
                    new_customer = Customer(uid, self)
                    new_customer.lifetime=type_customer.lifetime
                    new_customer.preference_list=type_customer.preference_list
                    new_customer.seller_preferencelist=type_customer.seller_preferencelist
                    new_customer.type_name=type_customer.type_name
                    self.grid.place_agent(new_customer,self.grid.find_empty())
                    self.schedule.add(new_customer)
                    self.customers.append(new_customer)
                    uid =uid + 1
                    customer_generated=1+customer_generated
            self.number_of_customer = customer_generated
        else:
            for i in range(self.number_of_customer):
                new_customer = Customer(i, self)
                self.grid.place_agent(new_customer,self.grid.find_empty())
                self.schedule.add(new_customer)
                self.customers.append(new_customer)    
    def create_sellers(self):
        self.sellers =[]
        for i in range(self.number_of_seller):
            new_seller = Seller(i, self)
            self.grid.place_agent(new_seller,self.grid.find_empty())
            # self.schedule.add(new_seller)
            self.sellers.append(new_seller)
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
if __name__ == "__main__":


    market1 = Market()
    # c1= Customer(1,market1) 
    # # market1.gen_rand_productlist(min_price=100000,price_interval=300000,number=50)
    # market1.gen_usercsv_productlist(file_path="file.csv")
    # print(market1.product_list)
    # # for i in range(10):
        # c1.step()
        # s1=Seller(i,market1)

