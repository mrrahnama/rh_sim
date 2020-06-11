import random

from mesa.agent import Agent

class Customer(Agent):

    def __init__(self, unique_id, model, pos=None):
        super().__init__(unique_id, model)
        self.pos = pos
        self.preference_list =["p1","p2","p3","p4","0"]
        # self.move = {"stick": self.stick,
        #             "switch": self.switch,
        #             }
        random.shuffle(self.preference_list)
    def step(self):
        pass
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


    def find_food(self):
        neig = self.model.grid.get_neighbors(self.pos, True, False)
        if neig:
            agent = random.choice(neig)
            if isinstance(agent, Food):
                self.eat(agent)

    def eat(self, food):
        gain = self.age * self.metabolism
        self.energy += gain
        food.energy -= gain

    def die(self):
        self.model.grid._remove_agent(self.pos, self)
        self.model.schedule.remove(self)
        self.model.number_of_bug -= 1

