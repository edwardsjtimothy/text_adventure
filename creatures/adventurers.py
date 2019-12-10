#random number module
import random
#import monster classes
from monsters import *

#player classes

#wizard class 
class Wizard: 
    name = ""
    health = 0
    mana = 0

    def __init__(self, me, hp, mn):
        self.name = me 
        self.health = hp + random.randrange(5, 15)
        self.mana = mn + random.randrange(20, 40)


#rogue class
class Rogue:
    name = ""
    health = 0
    focus = 0

    def __init__(self, me, hp, fc):
        self.name = me 
        self.health = hp + random.randrange(10, 20)
        self.focus = fc + random.randrange(10, 20)


#barbarian class
class Barbarian:       
    name = ""
    health = 0
    rage = 0

    def __init__(self, me, hp, rg):
        self.name = me 
        self.health = hp + random.randrange(20, 30)
        self.rage = rg + random.randrange(10, 20)




    
       
    