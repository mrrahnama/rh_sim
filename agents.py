import random
from mesa.space import SingleGrid,MultiGrid
from mesa.agent import Agent

class Product:
    def __init__(self, name, minvalue,offervalue=0,avilable=1):
        self.name=name
        self.minvalue=minvalue
        self.sold =0
        self.offervalue=minvalue
        if self.offervalue>0:
            self.offervalue=offervalue
        self.avilable=avilable
        


class Seller(Agent):

    def __init__(self, unique_id, model, pos=None):
        super().__init__(unique_id, model)
        self.pos = pos
        self.inventory =dict( {"p"+str(i) :Product("p"+str(i) ,i*100+80) for i in range(1,5)})
        self.strategy="DF"
        self.revenue=0
        self.profit=0
        # "Goal-Directed" or "Derivative-Following"
        if not(self.strategy in ["GD", "DF"]):
            raise TypeError("'strategy' must be one of {Goal-Directed->GD or Derivative-Following ->DF}")
       
    def step(self):
        pass
    def sell(self,customer,product_name,price):
        p=self.inventory.get(product_name)
        if p.avilable>0:
            p.sold+=1
            p.avilable-=1
            self.revenue+=price
            self.profit+= price-p.minvalue
            return True
        else:
            return False

class DF_seller (Seller):

    density = 0.005
    growth_rate = 4
    wilt_rate = 2
    max_growth = 20
    energy = 4

class dd_seller(Seller):

    density = 0.01
    growth_rate = 2
    wilt_rate = 1
    max_growth = 10
    energy = 2

class Customer(Agent):

    def __init__(self,unique_id,model,pos=None):
        super().__init__(unique_id, model)
        self.pos = pos
        self.preference_list = {"p1":random.randint(100,200),
        "p2":random.randint(200,300),
        "p3":random.randint(300,400),
        "p4":random.randint(400,500)
        }
        self.dietime=2
        items=list(self.preference_list.items())
        random.shuffle(items)
        self.preference_list=dict(items)
        self.alive=True
        # self.preference_list={(key, self.preference_list[key]) for key in keyss}
        # random.shuffle(self.preference_list)
  
    def move_to(self, pos):
        self.model.grid.move_agent(self, pos)

    def switch(self):
        neig = self.model.grid.get_neighborhood(self.pos, True, False)
        pos = random.choice(neig)
        if self.model.grid.is_cell_empty(pos):
            self.move_to(pos)

    def stick(self):
        neig = self.model.grid.get_neighbors(self.pos, True)
        if not(neig):
            pos = self.model.grid.find_empty()
            self.move_to(pos)


    def find_store(self):
        agent = random.choice(self.model.sellers)
        pos=self.model.grid.get_neighborhood(agent.pos, False)
        for p in pos:
            if self.model.grid.is_cell_empty(p):
                self.move_to(p)
                return agent
            # if isinstance(agent, Seller):
            #     self.eat(agent)
        return 0

    def buy(self, seller : Seller):
        for p in self.preference_list:
                if p in seller.inventory:
                    if self.preference_list.get(p) <= seller.inventory.get(p).minvalue:
                        price=(self.preference_list.get(p)+seller.inventory.get(p).minvalue)/2
                        if seller.sell(self,p,price):
                            print(str(self.unique_id)+"  customer buy "+str(p))
                            self.alive=False
                            break
        self.model.grid.move_to_empty(self)            

    def die(self):
        self.model.grid._remove_agent(self.pos, self)
        self.model.schedule.remove(self)
        self.model.number_of_customer -= 1
    def step(self):
        if self.alive:
            seller =self.find_store()
            if seller:
                self.buy(seller)
        else:
            self.dietime -=1
            if not self.dietime>0:
                self.die()

        


