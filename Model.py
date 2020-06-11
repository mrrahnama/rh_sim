from mesa.model import Model
from mesa.space import SingleGrid,MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from agents import Customer,Seller
class Market(Model):
    def __init__(self, width=20, height=20, num_customer=50,num_seller=4):
        # super().__init__(self,seed=seed)
        self.number_of_customer = num_customer
        self.number_of_seller = num_seller
        self.grid = MultiGrid(width, height, False)
        self.schedule = RandomActivation(self)
        self.running=True
        self.customers=[]
        self.sellers=[]
        self.create_sellers()
        self.create_customers()
        data = {"Customer": lambda m: m.number_of_customer,
                "Seller": lambda m: m.number_of_seller,
                }
        data2 = {"s1": lambda m: m.revenue,
        "s2": lambda m: m.revenue,

        }
        self.datacollector = DataCollector(data)
        self.datacollector.collect(self)
    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
        if not(self.grid.exists_empty_cells()):
            self.running = False

    def create_customers(self):
        for i in range(self.number_of_customer):
            new_customer = Customer(i, self)
            self.grid.place_agent(new_customer,self.grid.find_empty())
            self.schedule.add(new_customer)
            self.customers.append(new_customer)
        
    def create_sellers(self):
        for i in range(self.number_of_seller):
            new_seller = Seller(i, self)
            self.grid.place_agent(new_seller,self.grid.find_empty())
            self.schedule.add(new_seller)
            self.sellers.append(new_seller)

if __name__ == "__main__":
    market1 = Market()
    for i in range(10):
        c1= Customer(i,market1) 
        c1.step()
        s1=Seller(i,market1)


