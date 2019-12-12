#random number module
import random
import math

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
            self.mana += random.randrange(1, 4)
            if self.mana > self.maxMana:
                self.mana = self.maxMana


#basic attack
    def melee(self, target):
        hit = random.randrange(1, 21)
        dmg = 1 + random.randrange(1, 4)
        crit = dmg * 2
        print("hit roll", hit)

        #mana regen
        self.manaRegen()

        if 10 < hit < 20:
            target.health -= dmg
            print(f"Your target took {dmg} damage!")
        elif hit == 20: 
            target.health -= crit
            print(f"Critical strike! Your target took {dmg} damage!")
        elif hit < 11:
            print("Your attack failed to damage the target...")


#fireball spell
    def fireball(self, target):
        hit = random.randrange(1, 21)
        dmg = random.randrange(5, 11)
        burn =  math.floor(dmg * 0.75)
        crit = dmg * 2
        print("hit roll", hit)

        #mana regen
        self.manaRegen()

        if self.mana < 5:
            print("Insufficient mana!")
            return
        elif self.mana >= 5:
            self.mana -= 5
            if 5 < hit < 16 :
                target.health -= dmg
                print(f"Your target took {dmg} damage!")
            elif 15 < hit < 20:
                target.health -= (dmg + burn)
                print(f"With a crackle of rising flames you target catches on fire! Your target took {dmg} damage and burns for an additional {burn}!")
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

        print("Snaking threads of arcane power bring knowledge of your foe...")
        print(f"""
            ||Name: {target.name} ||
            ||Health: {target.health} ||
            ||stam: {target.stamina} ||
        """)


#rogue class
class Rogue:
    name = ""
    health = 0
    focus = 0
    maxFocus = 0
    cloaked = False

    def __init__(self, me, hp, fc):
        self.name = me 
        self.health = hp + random.randrange(10, 21)
        self.focus = fc
        self.maxFocus = self.focus

    def focusRegen(self):
        if self.focus < self.maxFocus:
            self.focus += random.randrange(2, 5)
            if self.focus > self.maxFocus:
                self.focus = self.maxFocus

#basic attack
    def melee(self, target):
        self.cloaked = False
        hit = random.randrange(1, 21)
        dmg = 2 + random.randrange(2, 5)
        crit = dmg * 2
        print("hit roll", hit)

        #focus regen
        self.focusRegen()

        if 5 < hit < 20:
            target.health -= dmg
            print(f"Your target took {dmg} damage!")
        elif hit == 20: 
            target.health -= crit
            print(f"Critical strike! Your target took {dmg} damage!")
        elif hit < 6:
            print("Your attack failed to damage the target...")

#main ability with high crit dmg
    def punchingStab(self, target):
        self.cloaked = False
        hit = random.randrange(1, 21)
        dmg = random.randrange(8, 13)
        crit = math.floor(dmg * 2.5)
        print("hit roll", hit)

        #focus regen
        self.focusRegen()

        #ability cost and effect
        if self.focus < 20:
            print("Insufficient focus!")
            return
        elif self.focus >= 20:
            self.focus -= 20
            if 5 < hit < 20:
                target.health -= dmg
                print(f"Your target took {dmg} damage!")
            elif hit == 20: 
                target.health -= crit
                print(f"Critical strike! Your target took {dmg} damage!")
            elif hit < 6:
                print("Your attack failed to damage the target...")

    def cloakofShadows(self, target):
        self.cloaked = False

        #focus regen
        self.focusRegen()

        #ability cost and effect
        if self.focus < 10:
            print("Insufficient focus!")
            return
        elif self.focus >= 10:
            self.focus -= 10
            self.cloaked = True
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
        self.health = hp + random.randrange(20, 31)
        self.maxRage = rg + random.randrange(10, 21)
        self.rage = 0

    def rageGen(self):
         hMRG = random.randrange(5, 8)
         if self.rage < self.maxRage:
            self.rage += hMRG
            print(f"You generated {hMRG} rage!")
            if self.rage > self.maxRage:
                self.rage = self.maxRage

# basic attack
    def melee(self, target):
        hit = random.randrange(1, 21)
        dmg = 2 + random.randrange(3, 6)
        crit = dmg * 2

        #focus regen
        self.rageGen()

        if 5 < hit < 20:
            target.health -= dmg
            print(f"Your target took {dmg} damage!")
        elif hit == 20: 
            target.health -= crit
            print(f"Critical strike! Your target took {dmg} damage!")
        elif hit < 6:
            print("Your attack failed to damage the target...")

    def savageBlow(self, target):
        hit = random.randrange(1, 21)
        dmg = math.floor(2 + random.randrange(3, 6) + (self.rage / 5))
        crit = dmg * 2
        self.rage = 0
        print("hit roll", hit)
           
        if 5 < hit < 20:
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