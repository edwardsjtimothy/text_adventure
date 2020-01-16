#random number module
import random
#math module for stat calculation
import math
#system module to kill program upon character death
import sys
#loot tables 
from misc import wizardLoot

#player classes

#wizard class 
class Wizard: 
    name = ""
    health = 0
    mana = 0
    maxMana = 0
    maneuvered = False
    pyroBrand = False
    inventory = []

    def __init__(self, me, hp, mn):
        self.name = me 
        self.health = hp + random.randrange(5, 15)
        self.mana = mn + random.randrange(20, 40)
        self.maxMana = self.mana
        self.maneuvered = False
        self.pyroBrand = False
        self.inventory = []

#function to check character stats and conditional states
    def pulseCheck(self):
        if self.pyroBrand == True:
            pyro = "Active"
        elif self.pyroBrand == False:
            pyro = "Inactive"

        if self.maneuvered == True:
            mane = "Active"
        elif self.maneuvered == False:
            mane = "Inactive"
       
        print(f"""
            ||Name: {self.name} ||
            ||Health: {self.health} ||
            ||Mana: {self.mana} ||
            ||Pryobrand: {pyro} ||
            ||Maneuver: {mane} ||
        """)

#mana regeneration function 
    def manaRegen(self):
        ma = random.randrange(3, 6)
        if self.mana < self.maxMana:
            self.mana += ma
            print(f"You generate {ma} mana.")
        if self.mana > self.maxMana:
            self.mana = self.maxMana

#basic attack
    def melee(self, target):
        hit = random.randrange(1, 21)
        dmg = 1 + random.randrange(1, 4)
        crit = dmg * 2

        if self.maneuvered == True:
            hit = random.randrange(10, 21)
            self.maneuvered = False

        #mana regen
        self.manaRegen()

        if 7 < hit < 20:
            target.health -= dmg
            print(f"Your target took {dmg} damage!")
        elif hit == 20: 
            target.health -= crit
            print(f"Critical strike! Your target took {crit} damage!")
        elif hit < 8:
            print("Your attack failed to damage the target...")

#fireball spell
    def fireball(self, target):
        hit = random.randrange(1, 21)
        dmg = random.randrange(5, 16)
        burn =  math.floor(dmg * 0.75)
        crit = dmg * 2

        # checking for maneuvered and pyrobrand states and applying buffs
        if self.maneuvered == True and self.pyroBrand == False:
            hit = random.randrange(10, 21)
            self.maneuvered = False
        elif self.maneuvered == False and self.pyroBrand == True:
            burn = math.floor(dmg * random.randrange(1 , 4))
            self.maneuvered = False
        elif self.maneuvered == True and self.pyroBrand == True: 
            hit = random.randrange(10, 21)
            burn = math.floor(dmg * random.randrange(1 , 5))
            self.maneuvered = False

        #mana regen
        self.manaRegen()

        if self.mana < 10:
            print("Insufficient mana!")
            return
        elif self.mana >= 10:
            self.mana -= 10
            if 4 < hit < 16 :
                target.health -= dmg
                print(f"Your target took {dmg} damage!")
            elif 15 < hit < 20:
                target.health -= (dmg + burn)
                print(f"With a crackle of rising flames your target catches on fire! Your target took {dmg} damage and burns for an additional {burn}!")
                self.pyroBrand = False
            elif hit == 20: 
                target.health -= (crit + burn)
                print(f"Critical strike! Your target took {crit} damage and burns for an additional {burn}!")
                self.pyroBrand = False
            elif hit < 5:
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
            self.pyroBrand = True
            print("Snaking threads of arcane power bring knowledge of your foe...")
            print(f"""
                ||Name: {target.name} ||
                ||Health: {target.health} ||
                ||stam: {target.stamina} ||
            """)
            print("Your prodigious will influences the warp and weft of reality around your target and the air crackles with motive force. Your scrutiny has applied Pryobrand!")

# check if the player is dead and end game if true
    def deathCheck(self):
        if self.health <= 0:
            print(f"In the seconds before the killing blow is struck, your mind races as you cast frantically around for a spell or a scrape of untapped power that may yet save you. But you know it is for nothing. The blow lands and you fall to your knees in the dust. The magic flickers and dies from your fingers, and its light fades with the light in your eyes. Someone may yet attain the knowledge hidden in this place but it will not be you. Die well, {self.name}.")
            exit("**********Game Over**********")

# maneuver to attempt to gain an advantage against your foe
    def maneuver(self):
        self.maneuvered = False
        adAtmp = random.randrange(1, 21)
        #mana regen
        self.manaRegen()
        if adAtmp > 10:
            self.maneuvered = True
            print("You edge carefully around your opponent, arm held before you with fingers curled in a casting posture. Flame roils around your hand and up your arm, livid with the potency of your acane power held in abeyance. You wait for an opening. You have spotted a weakness!")
        elif adAtmp < 11:
            print("You circle warily around your opponent, searching for weaknesses with a preternatural eye. You find none.")

# loot function to see if items drop from encounters
    def loot(self, lt, ir):
        # parameters allow adjustment how likely it is for 1) an item to drop 2) how rare the item could be if something does drop 
        anyLoot = random.randrange(lt, 21)
        dHundo = random.randrange(ir, 101)

        if anyLoot >= 17:
            print("Loot has dropped!")
            if 1 < dHundo < 86:
                item = wizardLoot("common")
                print(f"{item} has been added to your inventory!")
                self.inventory.append(item)
            if 85 < dHundo < 99:
                item = wizardLoot("rare")
                print(f"{item} has been added to your inventory!")
                self.inventory.append(item)
            if 98 < dHundo < 101:
                item = wizardLoot("wondrous")
                print(f"{item} has been added to your inventory!")
            


#rogue class
class Rogue:
    name = ""
    health = 0
    focus = 0
    maxFocus = 0
    maneuvered = False
    shaStk = False

    def __init__(self, me, hp, fc):
        self.name = me 
        self.health = hp + random.randrange(10, 21)
        self.maxFocus = fc
        self.focus = math.floor(fc / 2)
        self.maneuvered = False
        self.shaStk = False

#function to check character stats and conditional states
    def pulseCheck(self):
        if self.maneuvered == True:
            mane = "Active"
        elif self.maneuvered == False:
            mane = "Inactive"

        print(f"""
            ||Name: {self.name} ||
            ||Health: {self.health} ||
            ||Focus: {self.focus} ||
            ||Maneuver: {mane} ||
        """)

# focus regeneration function
    def focusRegen(self):
        fc = random.randrange(5, 8)
        if self.focus < self.maxFocus:
            self.focus += fc
            print(f"You generate {fc} focus.")
        if self.focus > self.maxFocus:
            self.focus = self.maxFocus

#basic attack
    def melee(self, target):
        hit = random.randrange(1, 21)
        dmg = 2 + random.randrange(2, 5)
        crit = dmg * 2

        if self.maneuvered == True:
            hit = random.randrange(10, 21)
            self.maneuvered = False

        if self.shaStk == True:
            hit = 20
            crit = math.floor(dmg * 3)
            self.shaStk = False

        #focus regen
        self.focusRegen()

        if 4 < hit < 20:
            target.health -= dmg
            print(f"Your target took {dmg} damage!")
        elif hit == 20: 
            target.health -= crit
            print(f"Critical strike! Your target took {crit} damage!")
        elif hit < 5:
            print("Your attack failed to damage the target...")

#main ability with high crit dmg
    def punchingStab(self, target):
        hit = random.randrange(1, 21)
        dmg = 5 + random.randrange(8, 13)
        crit = math.floor(dmg * 2)

        # checking for conditional states and applying buffs
        if self.maneuvered == True:
            hit = random.randrange(10, 21)
            self.maneuvered = False

        if self.shaStk == True:
            hit = 20
            crit = math.floor(dmg * 3)
            self.shaStk = False

        #focus regen
        self.focusRegen()

        #ability cost and effect
        if self.focus < 20:
            print("Insufficient focus!")
            return
        elif self.focus >= 20:
            self.focus -= 20
            if 4 < hit < 19:
                target.health -= dmg
                print(f"Your target took {dmg} damage!")
            elif hit >= 18: 
                target.health -= crit
                print(f"Critical strike! Your target took {crit} damage!")
            elif hit < 5:
                print("Your attack failed to damage the target...")

# Strike with 100% crit chance. Enemy can't retaliate.
    def shadowStrike(self, target):
        #focus regen
        self.focusRegen()

        #ability cost and effect
        if self.focus < 60:
            print("Insufficient focus!")
            return
        elif self.focus >= 60:
            self.focus -= 60
            self.shaStk = True
            if self.focus >= 20:
                print("Wisps of shadow flow about you, obscuring your second Punching Stab from the enemy!")
                self.punchingStab(target)
            elif self.focus <= 20:
                print("Wisps of shadow flow about you, obscuring your second Melee attack from the enemy!")
                self.melee(target)

# check if the player is dead and end game if true
    def deathCheck(self):
        if self.health <= 0:
            print(f"Your eyes go wide a well placed thrust from your foe sends the point of its jagged blade beneath your guard and between your ribs. You fall to the ground, weapons clattering on the ancient flagstones, lifeblood flowing in a widening pool around you. All your careful planning, all your stealth and skill, none of it prepared you for the creeping darkness of this place. Someone may yet plumb its depths and turn out its secrets but it will not be you. Die well, {self.name}.")
            exit("**********Game Over**********")

# maneuver to attempt to gain an advantage against your foe
    def maneuver(self):
        self.maneuvered = False
        adAtmp = random.randrange(1, 21)

        #focus regen
        self.focusRegen()

        if adAtmp > 10:
            self.maneuvered = True
            print("Crouching low with daggers held before you in a dueling posture, you edge closer to your foe. Shadow flows around you as you gather yourself for a precision strike. You have spotted a weakness!")
        elif adAtmp < 11:
            print("You circle your foe warily, observing as much as you can about your target, searching for a weakness. You find none.")


#barbarian class
class Barbarian:       
    name = ""
    health = 0
    rage = 0
    maxRage = 0
    maneuvered = False

    def __init__(self, me, hp, rg):
        self.name = me 
        self.health = hp + random.randrange(20, 31)
        self.maxRage = rg + random.randrange(10, 21)
        self.rage = 0
        self.maneuvered = False

#function to check character stats and conditional states
    def pulseCheck(self):
        if self.maneuvered == True:
            mane = "Active"
        elif self.maneuvered == False:
            mane = "Inactive"
       
        print(f"""
            ||Name: {self.name} ||
            ||Health: {self.health} ||
            ||Rage: {self.rage} ||
            ||Maneuver: {mane} ||
        """)

#rage generation function 
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

        # checking for conditional states
        if self.maneuvered == True:
            hit = random.randrange(10, 21)
            self.maneuvered = False

        #focus regen
        self.rageGen()

        if 4 < hit < 20:
            target.health -= dmg
            print(f"Your target took {dmg} damage!")
        elif hit == 20: 
            target.health -= crit
            print(f"Critical strike! Your target took {crit} damage!")
        elif hit < 5:
            print("Your attack failed to damage the target...")

# spends rage for extra dmg at a 3rg/1dmg ratio
    def savageBlow(self, target):
        hit = random.randrange(1, 21)
        dmg = math.floor(random.randrange(9, 14) + (self.rage / 3))
        crit = dmg * 2
        self.rage = 0

        if self.maneuvered == True:
            hit = random.randrange(10, 21)
            self.maneuvered = False

        print("hit roll", hit)
           
        if 4 < hit < 20:
            target.health -= dmg
            print(f"Your target took {dmg} damage!")
        elif hit == 20: 
            target.health -= crit
            print(f"Critical strike! Your target took {crit} damage!")
        elif hit < 5:
            print("Your attack failed to damage the target...")

        
    def mortalStrike(self, target):
        dmg = 6 + random.randrange(6, 9)

        if self.maneuvered == True:
            dmg = 9 + random.randrange(7, 10)
            self.maneuvered = False

        if self.rage < 50:
            print("Insufficient rage!")
            return
        elif self.rage >= 50:
            self.rage -= 50
            if target.health < math.floor(target.maxHealth / 3):
                target.health = 0
                print("Your weapon cleaves through the air in a vicious arc; your enemy withers beneath the strength of your blow.")
            elif target.health > math.floor(target.maxHealth / 3):
                target.health -= dmg
                print(f"Your weapon cleaves through the air in a vicious arc; your oppenent deflects the strike and stumbles back, avoiding the worst of the damage. You deal {dmg} damage!")

# check if the player is dead and end game if true
    def deathCheck(self):
        if self.health <= 0:
            print(f"You fall heavily to your knees and your weapon slips from numb fingers to clatter against the ancient flagstones. Your strength is broken. Your vision blurs and your rage fades to nothing, leaving you empty. Your enemies surround you, dark silhouettes backlit by the guttering light of your fallen torch. Someone may yet lay bare the mystery of this place but it will not be you. Die well, {self.name}.")
            exit("**********Game Over**********")   

    def maneuver(self):
        self.maneuvered = False
        adAtmp = random.randrange(1, 21)

        if adAtmp > 10:
            self.maneuvered = True
            print("Loosing a feral snarl, you prepare to rush forward and bring your weapon down upon your hapless foe with the precision born of your brutal skill. You have spotted a weakness!")
        elif adAtmp < 11:
            print("Your weapon poised wardlingly in front of you, you circle your oppenent searching for a weakness. You find none.")
