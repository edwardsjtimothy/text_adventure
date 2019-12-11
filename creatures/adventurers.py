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
    maxMana = 0

    def __init__(self, me, hp, mn):
        self.name = me 
        self.health = hp + random.randrange(5, 15)
        self.mana = mn + random.randrange(20, 40)
        self.maxMana = self.mana

#mana regeneration function 
    def manaRegen(self):
        if self.mana < self.maxMana:
            self.mana += random.randrange(1, 3)
            if self.mana > self.maxMana:
                self.mana = self.maxMana

#melee combat function
    def melee(self, target):
        hit = random.randrange(1, 20)
        dmg = 1 + random.randrange(1, 3)
        crit = dmg * 2

        #mana regen
        # self.manaRegen(self)

        if hit > 10:
            target.health -= dmg
            message = "Your target took {} damage!"
            print(message.format(dmg))
        elif hit == 20: 
            target.health -= crit
            message = "Critical strike! Your target took {} damage!"
            print(message.format(dmg))
        elif hit < 11:
            print("Your attack failed to damage the target...")


#fireball spell
    def fireball(self, target):
        hit = random.randrange(1, 20)
        dmg = random.randrange(5,10)
        crit = dmg * 2

        #mana regen
        # self.manaRegen()

        if self.mana < 5:
            print("Insufficient mana!")
        elif self.mana >= 5:
            self.mana -= 5
            if hit > 5:
                target.health -= dmg
                message = "Your target took {} damage!"
                print(message.format(dmg))
            elif hit == 20: 
                target.health -= crit
                message = "Critical strike! Your target took {} damage!"
                print(message.format(dmg))
            elif hit < 6:
                print("Your attack failed to damage the target...")

#gain information about your target
    def augury(self, target):
        #mana regen
        self.manaRegen()

        if self.mana < 15:
            print("Insufficient mana!")
        elif self.mana >= 15:
            self.mana -= 15

        target.stats = """
            ||Name: {} ||
            ||Health: {} ||
            ||stam: {} ||
        """
        print("Threads of arcane power bring knowledge of your foe...")
        print(target.stats.format(target.name, target.health, target.stamina))







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




    
       
    