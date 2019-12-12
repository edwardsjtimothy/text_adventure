#random number module
import random
#math module for stat calculation
import math
#system module to kill program upon character death
import sys

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
            print(f"Critical strike! Your target took {crit} damage!")
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
                print(f"Critical strike! Your target took {crit} damage!")
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

    def deathCheck(self):
        if self.health <= 0:
            print(f"In the seconds before the killing blow is struck, your mind races as you cast frantically around for a spell or a scrape of untapped power that may yet save you. But you know it is for nothing. The blow lands and you fall to your knees in the dust. The magic flickers and dies from your fingers, and its light fades with the light in your eyes. Someone may yet attain the knowledge hidden in this place but it will not be you. Die well, {self.name}")
            exit("**********Game Over**********")


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
            print(f"Critical strike! Your target took {crit} damage!")
        elif hit < 6:
            print("Your attack failed to damage the target...")

#main ability with high crit dmg
    def punchingStab(self, target):
        self.cloaked = False
        hit = random.randrange(1, 21)
        dmg = random.randrange(8, 13)
        crit = math.floor(dmg * 2)
        print("hit roll", hit)

        #focus regen
        self.focusRegen()

        #ability cost and effect
        if self.focus < 20:
            print("Insufficient focus!")
            return
        elif self.focus >= 20:
            self.focus -= 20
            if 5 < hit < 19:
                target.health -= dmg
                print(f"Your target took {dmg} damage!")
            elif hit >= 18: 
                target.health -= crit
                print(f"Critical strike! Your target took {crit} damage!")
            elif hit < 6:
                print("Your attack failed to damage the target...")

    def shadowStrike(self, target):
        self.cloaked = False

        #focus regen
        self.focusRegen()

        #ability cost and effect
        if self.focus < 60:
            print("Insufficient focus!")
            return
        elif self.focus >= 60:
            self.focus -= 60
            print("Wisps of shadow flow about you, obscuring your second strike from the enemy!")
            if self.focus >= 20:
                self.punchingStab(target)
            elif self.focus <= 20:
                self.melee(target)

    def deathCheck(self):
        if self.health <= 0:
            print(f"Your eyes go wide a well placed thrust from your foe sends the point of its jagged blade beneath your guard and between your ribs. You fall to the ground, weapons clattering on the ancient flagstones, lifeblood flowing in a widening pool around you. All your careful planning, all your stealth and skill, none of it prepared you for the creeping darkness of this place. Someone may yet plumb its depths and turn out its secrets but it will not be you. Die well, {self.name}.")
            exit("**********Game Over**********")

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
            print(f"Critical strike! Your target took {crit} damage!")
        elif hit < 6:
            print("Your attack failed to damage the target...")

# spends rage for extra dmg at a 3rg/1dmg ratio
    def savageBlow(self, target):
        hit = random.randrange(1, 21)
        dmg = math.floor(random.randrange(9, 14) + (self.rage / 3))
        crit = dmg * 2
        self.rage = 0
        print("hit roll", hit)
        print(dmg)
           
        if 5 < hit < 20:
            target.health -= dmg
            print(f"Your target took {dmg} damage!")
        elif hit == 20: 
            target.health -= crit
            print(f"Critical strike! Your target took {crit} damage!")
        elif hit < 6:
            print("Your attack failed to damage the target...")

        
    def mortalStrike(self, target):
        dmg = 6 + random.randrange(6, 9)

        if self.rage < 50:
            print("Insufficient rage!")
            return
        elif self.rage >= 50:
            self.rage -= 50
            if target.health < math.floor(target.maxHealth / 3):
                target.health = 0
                print("Your weapon cleaves through the air in a vicious arch; your enemy withers beneath the strength of your blow.")
            elif target.health > math.floor(target.maxHealth / 3):
                target.health -= dmg

    def deathCheck(self):
        if self.health <= 0:
            print(f"You fall heavily to your knees and your weapon slips from numb fingers to clatter against the ancient flagstones. Your strength is broken. Your vision blurs and your rage fades to nothing, leaving you empty. Your enemies surround you, dark silhouettes backlit by the guttering light of your fallen torch. Someone may yet lay bare the mystery of this place but it will not be you. Die well, {self.name}.")
            exit("**********Game Over**********")   
