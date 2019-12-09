#random number module
import random

#player classes

class Wizard: 
    health = 10 + random.randrange(1,10)
    mana = 20 + random.randrange(10,30)