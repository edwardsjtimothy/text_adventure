#random number module
import random

#player classes

class Wizard: 
    name = ""
    health = 0
    mana = 0

    def __init__(self, me, hp, mn):
        self.name = me 
        self.health = hp + random.randrange(5, 15)
        self.mana = mn + random.randrange(20, 40)

    # def display(self): 
    #     print("Health = " + str(self.health) + random.randrange(5, 15)) 
    #     print("Mana = " + str(self.mana) + random.randrange(20, 40)) 

    
       
    