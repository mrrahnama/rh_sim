import pickle

from numpy import random
from random import shuffle
import random as rnn

from mesa.agent import Agent



class Product:
    def __init__(self, name, minvalue, offer_value=0, available=2):
        self.name = name
        self.minvalue =float(minvalue)
        self.sold = 0
        self.offervalue = float(minvalue )* 1.15
        if float(offer_value) > 0:
            self.offervalue = float(offer_value)
        self.available =int(available)
        self.initial = self.available


class Negotiation:

    def __init__(self, step, seller, customer,cstype, product, timestamp, cost, status=1):
        self.step = step
        self.seller = seller
        self.customer = customer
        self.product = product
        self.timestamp = timestamp
        self.cost = cost
        self.customer_type = cstype
        if status == 1:
            self.status = "SUCCESS"
        elif status == 2:
            self.status = "FAILED_PRICE"
        elif status == 3:
            self.status = "FAILED_EMPTY"
        elif status == 4:
            self.status = "NOT_EXIST"

class Seller(Agent):
    def __init__(self, unique_id, model,name='', pos=None,inventory=None):
        super().__init__(unique_id, model)
        self.pos = pos
        self.revenuebystep=[]
        self.laststepinffo={"revenue":0}
        self.inventory_count = 0
        if inventory is None:
            self.inventory = {}
            for i in range(1, 5):
                self.inventory["p" + str(i)] = Product("p" + str(i), random.randint(1, 100) + i * 100, available=random.randint(2, 20))
        else :
            self.inventory=inventory
        self.inventory_available()
        # self.strategy = "self.strategy15"
        # self.strategy = strategy15(self,0.15)

        self.revenue = 0
        self.profit = 0
        # self.transactions =[]
        # self.conversatoins=[]
        # "Goal-Directed" or "Derivative-Following"
        self.succesful_transaction = 0
        self.failed_transaction = 0
        if name is '':
            self.name=str(self.unique_id)
        else:
            self.name=name
        self.model=model
        # if not (self.strategy in ["GD", "DF"]):
        #     raise TypeError(
        #         "'strategy' must be one of {Goal-Directed->GD or Derivative-Following ->DF}")

    def inventory_available(self):
        self.inventory_count = 0
        for p in self.inventory.values():
            self.inventory_count += p.available
        return self.inventory_count

    def step(self):
        pass

    def strategy15(self,product,step,percent = 0.15):
        productname=product.name
        return self.inventory[productname].minvalue*(1+percent)
    def strategy(self,product,step,percent = 0.15):
        productname=product.name
        return self.inventory[productname].minvalue*(1+percent)
    def isavilable(self,product_name):
        if product_name in self.inventory:
            p = self.inventory.get(product_name)
            if p.available > 0:
                return True
        return False

    def sell(self, customer, product_name, price):
        p = self.inventory.get(product_name)
        if p.available > 0:
            p.sold += 1
            p.available -= 1
            self.revenue += price
            self.profit += price - p.minvalue
            return True
        else:
            return False

    def GF_strategy(self, product) -> int:
        expsoldi = self.model.schedule.steps * \
                   (product.initial / self.model.max_steps)
        scalei = self.model.max_steps / 2 * \
                 (self.model.max_steps - self.model.schedule.steps)
        price = product.offervalue + product.offervalue * \
                ((product.sold - expsoldi) / expsoldi) * scalei
        return price

    def DF_strategy(self, product):
        pass


class strategy15(object):
    def __init__(self, seller: Seller, percent:float = 0.15):
        self.seller=seller
        self.percentage = percent
    def __call__(self,productname:Product,step:int):
        return productname.minvalue * self.percentage


class DFSeller(Seller):
    density = 0.005
    growth_rate = 4
    wilt_rate = 2
    max_growth = 20
    energy = 4


class DDSeller(Seller):
    density = 0.01
    growth_rate = 2
    wilt_rate = 1
    max_growth = 10
    energy = 2


class Customer(Agent):

    def __init__(self, unique_id: int, model, pos=None, lifetime=3):
        super().__init__(unique_id, model)
        self.pos = pos
        self.lifetime = lifetime
        self.seller_preferencelist = []
        self.alive = True
        self.leave = False
        self.percentofall = []
        self.type_name = ""
        self.tryNo=0

    def move_to(self, pos):
        self.model.grid.move_agent(self, pos)

    def switch(self):
        neig = self.model.grid.get_neighborhood(self.pos, True, False)
        pos = random.choice(neig)
        if self.model.grid.is_cell_empty(pos):
            self.move_to(pos)

    def stick(self):
        neig = self.model.grid.get_neighbors(self.pos, True)
        if not (neig):
            pos = self.model.grid.find_empty()
            self.move_to(pos)

    def find_store(self):
        agent = random.choice(list(self.model.sellers.values()))
        pos = self.model.grid.get_neighborhood(agent.pos, False)
        for p in pos:
            if self.model.grid.is_cell_empty(p):
                self.move_to(p)
                return agent
            # if isinstance(agent, Seller):
            #     self.eat(agent)
        return False

    def buy(self, seller: Seller):
        self.tryNo += 1
        for p in self.preference_list:

            if p in seller.inventory:

                price = seller.strategy(seller.inventory[p],self.model.schedule.steps)
                # price = seller.inventory.get(p).offervalue
                if (self.preference_list.get(p) >= price) and (seller.isavilable(p)):
                    seller.sell(self, p, price)
                    # price=(self.preference_list.get(p)+seller.inventory.get(p).minvalue)/2
                    # if seller.sell(self, p, price):
                    # print(str(self.unique_id) + "  customer buy " + str(p)) #--log
                    self.model.transactions.append(Negotiation(
                        self.model.schedule.steps, seller.unique_id, self.unique_id,self.type_name, p, 1, price))
                    self.alive = False
                    seller.succesful_transaction += 1
                    # self.die()
                    # break
                    return True
                else:
                    if (self.preference_list.get(p) >= price):
                        st = 3  # inventory failed
                    else:
                        st = 2  # price failed
                    seller.failed_transaction += 1
                    self.model.transactions.append(Negotiation(
                        self.model.schedule.steps, seller.unique_id, self.unique_id, self.type_name, p, 1, price, st))
            else:
                st = 4  # NOT EXIST
            seller.failed_transaction += 1
            self.model.transactions.append(Negotiation(
                self.model.schedule.steps, seller.unique_id, self.unique_id, self.type_name, p, 1, 0, st))
        return False
    def continueporb(self):
        return self.conproblist[self.tryNo]
    def create_preferencelist(self):
        self.preference_list = {"p1": random.randint(100, 220),
                                "p2": random.randint(200, 350),
                                "p3": random.randint(300, 470),
                                "p4": random.randint(400, 590)
                                }
    def ignorShopping(self,tryNo):
        probb=self.model.customerTypesDic[self.type_name].getcontprob(tryNo)
        rn=rnn.random()
        # print(rn,probb,self.unique_id)
        if rn >  self.model.customerTypesDic[self.type_name].getcontprob(tryNo):
            return True
        return False
    def die(self):
        if self.model.grid is not None:
            self.model.grid._remove_agent(self.pos, self)
        self.model.schedule.remove(self)
        self.model.number_of_customer -= 1

    def step(self):
        # seller = self.find_store() /todo::this function doesn't handle non grid runs
        if isinstance(self.model.sellers,dict):
            my_sellers = list(self.model.sellers.values())
        else:
            my_sellers=self.model.sellers
        random.shuffle(my_sellers)
        for seller in my_sellers:
            if self.buy(seller) :
                self.die()
                return
            elif self.ignorShopping(self.tryNo):

                break


        self.lifetime -= 1
        if self.lifetime == 0:
            self.die()


# if __name__ == "__main__":