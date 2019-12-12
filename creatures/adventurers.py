#random number module
import random
import math
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


#basic attack
    def melee(self, target):
        hit = random.randrange(1, 20)
        dmg = 1 + random.randrange(1, 3)
        crit = dmg * 2

        #mana regen
        self.manaRegen()

        if hit > 10:
            target.health -= dmg
            print(f"Your target took {dmg} damage!")
        elif hit == 20: 
            target.health -= crit
            print(f"Critical strike! Your target took {dmg} damage!")
        elif hit < 11:
            print("Your attack failed to damage the target...")


#fireball spell
    def fireball(self, target):
        hit = random.randrange(1, 20)
        dmg = random.randrange(5,10)
        crit = dmg * 2

        #mana regen
        self.manaRegen()

        if self.mana < 5:
            print("Insufficient mana!")
            return
        elif self.mana >= 5:
            self.mana -= 5
            if hit > 5:
                target.health -= dmg
                print(f"Your target took {dmg} damage!")
            elif hit == 20: 
                target.health -= crit
                print(f"Critical strike! Your target took {dmg} damage!")
            elif hit < 6:
                print("Your attack failed to damage the target...")

#gain information about your target
    def augury(self, target):
        #mana regen
        self.manaRegen()

        if self.mana < 15:
            print("Insufficient mana!")
            return
        elif self.mana >= 15:
            self.mana -= 15

        print(f"""
            ||Name: {target.name} ||
            ||Health: {target.health} ||
            ||stam: {target.stamina} ||
        """)
        print("Snaking threads of arcane power bring knowledge of your foe...")


#rogue class
class Rogue:
    name = ""
    health = 0
    focus = 0
    maxFocus = 0

    def __init__(self, me, hp, fc):
        self.name = me 
        self.health = hp + random.randrange(10, 20)
        self.focus = fc
        self.maxFocus = self.focus

    def focusRegen(self):
        if self.focus < self.maxFocus:
            self.focus += random.randrange(2, 4)
            if self.focus > self.maxFocus:
                self.focus = self.maxFocus

#basic attack
    def melee(self, target):
        hit = random.randrange(1, 20)
        dmg = 2 + random.randrange(2, 4)
        crit = dmg * 2

        #focus regen
        self.focusRegen()

        if hit > 5:
            target.health -= dmg
            print(f"Your target took {dmg} damage!")
        elif hit == 20: 
            target.health -= crit
            print(f"Critical strike! Your target took {dmg} damage!")
        elif hit < 6:
            print("Your attack failed to damage the target...")

    def punchingStab(self, target):
        hit = random.randrange(1, 20)
        dmg = random.randrange(8,12)
        crit = dmg * 2

        #focus regen
        self.focusRegen()

        #ability cost and effect
        if self.focus < 20:
            print("Insufficient focus!")
            return
        elif self.focus >= 20:
            self.focus -= 20
            if hit > 5:
                target.health -= dmg
                print(f"Your target took {dmg} damage!")
            elif hit == 20: 
                target.health -= crit
                print(f"Critical strike! Your target took {dmg} damage!")
            elif hit < 6:
                print("Your attack failed to damage the target...")

    def cloakofShadows(self, target):
        global cloak
        cloak = False

        #focus regen
        self.focusRegen()

        #ability cost and effect
        if self.focus < 10:
            print("Insufficient focus!")
            return
        elif self.focus >= 10:
            self.focus -= 10
            cloak = True
            print("Wisps of shadow flow about you, obscuring your precise location from your target...the target's next attack has a reduced chance to hit!")
            #need to build a way to denoted cloaking in enemy constructors


#barbarian class
class Barbarian:       
    name = ""
    health = 0
    rage = 0
    maxRage = 0

    def __init__(self, me, hp, rg):
        self.name = me 
        self.health = hp + random.randrange(20, 30)
        self.maxRage = rg + random.randrange(10, 20)
        self.rage = 0

    def rageGen(self):
         hMRG = random.randrange(5, 7)
         if self.rage < self.maxRage:
            self.rage += hMRG
            print(f"You generated {hMRG} rage!")
            if self.rage > self.maxRage:
                self.rage = self.maxRage

# basic attack
    def melee(self, target):
        hit = random.randrange(1, 20)
        dmg = 2 + random.randrange(3, 5)
        crit = dmg * 2

        #focus regen
        self.rageGen()

        if hit > 5:
            target.health -= dmg
            print(f"Your target took {dmg} damage!")
        elif hit == 20: 
            target.health -= crit
            print(f"Critical strike! Your target took {dmg} damage!")
        elif hit < 6:
            print("Your attack failed to damage the target...")

    def savageBlow(self, target):
        hit = random.randrange(1, 20)
        dmg = math.floor(2 + random.randrange(3, 5) + (self.rage / 5))
        crit = dmg * 2
        self.rage = 0
           
        if hit > 5:
            target.health -= dmg
            print(f"Your target took {dmg} damage!")
        elif hit == 20: 
            target.health -= crit
            print(f"Critical strike! Your target took {dmg} damage!")
        elif hit < 6:
            print("Your attack failed to damage the target...")

        
    def mortalStrike(self, target):

        if self.rage < 50:
            print("Insufficient rage!")
            return
        elif self.rage >= 50:
            self.rage -= 50

        if target.health < math.floor(target.maxHealth / 2):
            target.health = 0
            print("Your weapon cleaves through the air in a vicious arch; your enemy withers beneath the strength of your blow.")

        
        




    
       
    