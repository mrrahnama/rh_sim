import random
from mesa.space import SingleGrid, MultiGrid
from mesa.agent import Agent
#from Model import Market


class Product:
    def __init__(self, name, minvalue, offervalue=0, available=2):
        self.name = name
        self. minvalue = minvalue
        self.sold = 0
        self.offervalue = minvalue*1.15
        if offervalue > 0:
            self.offervalue = offervalue
        self.available = available
        self.initial = available
class negotiation():

    def __init__(self, step, seller, customer, product, timestamp, cost, status=1):
        self.step = step
        self.seller = seller
        self.customer = customer
        self.product = product
        self.timestamp = timestamp
        self.cost = cost
        if status==1:
            self.status = "SUCCESS"
        elif status==2:
            self.status = "FAILED_PRICE"
        elif status == 3:
            self.status = "FAILED_EMPTY"

class Seller(Agent):
    def __init__(self, unique_id, model, pos=None):
        super().__init__(unique_id, model)
        self.pos = pos
        self.inventory_count = 0
        self.inventory = dict(
            {"p"+str(i): Product("p"+str(i), random.randint(1, 100)+i*100, available=random.randint(2, 20)) for i in range(1, 5)})
        self.inventory_available()
        self.strategy = "DF"
        self.revenue = 0
        self.profit = 0
        # self.transactions =[]
        # self.conversatoins=[]
        # "Goal-Directed" or "Derivative-Following"
        self.succesful_transaction = 0
        self.failed_transaction = 0
        if not(self.strategy in ["GD", "DF"]):
            raise TypeError(
                "'strategy' must be one of {Goal-Directed->GD or Derivative-Following ->DF}")

    def inventory_available(self):
        self.inventory_count = 0
        for p in self.inventory.values():
            self.inventory_count += p.available
        return self.inventory_count

    def step(self):
        pass

    def sell(self,customer, product_name, price):
        p = self.inventory.get(product_name)
        if p.available > 0:
            p.sold += 1
            p.available -= 1
            self.revenue += price
            self.profit += price-p.minvalue
            return True
        else:
            return False

    def GF_strategy(self, product) -> int:
        expsoldi = self.model.schedule.steps * \
            (product.initial/self.model.max_steps)
        scalei = self.model.max_steps/2 * \
            (self.model.max_steps-self.model.schedule.steps)
        price = product.offervalue + product.offervalue * \
            ((product.sold - expsoldi)/expsoldi)*scalei
        return price

    def DF_strategy(self, product):
       pass

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
    def __init__(self, unique_id, model, pos=None, lifetime=3):
        super().__init__(unique_id, model)
        self.pos = pos
        self.lifetime = lifetime
        self.create_preferencelist()
        self.seller_preferencelist = []
        items = list(self.preference_list.items())
        random.shuffle(items)
        self.preference_list = dict(items)
        self.alive = True
        self.leave = False
        self.percentofall = 0
        self.type_name = ""
        # self.preference_list={(key, self.preference_list[key]) for key in keyss}
        # random.shuffle(self.preference_list)
    # def __init__(self,unique_id,model,**kwarg):
    #     pass

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
        pos = self.model.grid.get_neighborhood(agent.pos, False)
        for p in pos:
            if self.model.grid.is_cell_empty(p):
                self.move_to(p)
                return agent
            # if isinstance(agent, Seller):
            #     self.eat(agent)
        return 0

    def buy(self, seller: Seller):

        for p in self.preference_list:

            if p in seller.inventory:

                price = seller.inventory.get(p).offervalue
                if (self.preference_list.get(p) >= price) and (seller.sell(self, p, price)):

                    # price=(self.preference_list.get(p)+seller.inventory.get(p).minvalue)/2
                    #if seller.sell(self, p, price):
                    print(str(self.unique_id)+"  customer buy "+str(p))
                    self.model.transactions.append(negotiation(
                        self.model.schedule.steps, seller.unique_id, self.unique_id, p, 1, price))
                    self.alive = False
                    seller.succesful_transaction += 1
                    break
                else:
                    if (self.preference_list.get(p) >= price):
                        st=3  #inventory failed
                    else:
                        st=2 #price failed
                    seller.failed_transaction += 1
                    self.model.transactions.append(negotiation(
                        self.model.schedule.steps, seller.unique_id, self.unique_id, p, 1, price, st))
        self.leave = True

    def create_preferencelist(self):
        self.preference_list = {"p1": random.randint(100, 220),
                                "p2": random.randint(200, 350),
                                "p3": random.randint(300, 470),
                                "p4": random.randint(400, 590)
                                }

    def die(self):
        self.model.grid._remove_agent(self.pos, self)
        self.model.schedule.remove(self)
        self.model.number_of_customer -= 1

    def step(self):
        if self.leave:
            self.model.grid.move_to_empty(self)
            self.leave = False
        elif  self.alive and self.lifetime > 0:
            seller = self.find_store()
            if seller:
                self.buy(seller)
                self.lifetime -= 1
        else:
            self.die()