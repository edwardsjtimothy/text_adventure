#random number module
import random
#import monster classes
from creatures.monsters import *

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

#melee combat function
    def melee(self, target):
        target.stats = """
            ||Name: {} ||
            ||Health: {} ||
            ||stam: {} ||
        """
        print(target.stats.format(target.name, target.health, target.stamina))
        hit = random.randrange(1, 20)
        dmg = 1 + random.randrange(1, 3)
        crit = dmg * 2
        print(hit)
        if hit > 14:
            print("Target hp", target.health)
            target.health - dmg
            message = "Your target took {} damage!"
            print(message.format(dmg))
            print("Target hp", target.health)
        elif hit == 20: 
            target.health - crit
            message = "Critical strike! Your target took {} damage!"
            print(message.format(dmg))
        elif hit < 15:
            print("Your attack failed to damage the target...")






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




    
       
    