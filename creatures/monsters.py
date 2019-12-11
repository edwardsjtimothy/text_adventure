#random number module
import random

class Skeleton:
    name: ""
    health: 0
    stamina: 0
    maxStamina: 0

    def __init__(self, me, hp, st):
        self.name = me 
        self.health = hp + random.randrange(5, 10)
        self.stamina = st + random.randrange(5, 10)
        self.maxStamina = self.stamina

    def staminaRegen(self):
        if self.stamina < self.maxStamina:
            self.stamina += random.randrange(1, 2)
            if self.stamina > self.maxStamina:
                self.stamina = self.maxStamina

#basic attack
    def bludgeon(self, target):
        hit = random.randrange(1, 20)
        dmg = 1 + random.randrange(1, 2)
        crit = dmg * 2

        #stamina regen
        self.staminaRegen()

        if hit > 12:
            target.health -= dmg
            message = "You took {} damage!"
            print(message.format(dmg))
        elif hit == 20: 
            target.health -= crit
            message = "Critical strike! You took {} damage!"
            print(message.format(dmg))
        elif hit < 13:
            print("Your enemy's attack missed!")

#stronger attack
    def lumberingStrike(self, target):
        hit = random.randrange(1, 20)
        dmg = 2 + random.randrange(2, 3)
        crit = dmg * 2

        #stamina regen
        self.staminaRegen()

        if self.stamina < 15:
            print("Insufficient stamina!")
        elif self.stamina >= 15:
            self.stamina -= 15

        if hit > 15:
            target.health -= dmg
            message = "You took {} damage!"
            print(message.format(dmg))
        elif hit == 20: 
            target.health -= crit
            message = "Critical strike! You took {} damage!"
            print(message.format(dmg))
        elif hit < 16:
            print("Your enemy's attack missed!")

#chance at collapsing at low health
    def collapse(self):

            if self.health < 7:
                collapse = random.randrange(1, 20)

                if collapse < 10:
                    self.health = 0 
                    print("The necrotic energy animating your target dispates with a sigh; it collapses with a dry rattle of rolling bones...")

#random ability selector
    def abilitySelect(self, ability1, ability2, ability3):
        whichAbility = random.randrange(1,6)

        if whichAbility == 1 or 2 or 3:
            ability1
        elif whichAbility == 4 or 5:
            ability2
        elif whichAbility == 6:
            ability3







ancientSkeleton = Skeleton("Ancient Skeleton", 5, 10)
crumblingSkeleton = Skeleton("Crumbling Skeleton", 3, 7)
giantSkeleton = Skeleton("Giant Skeleton", 10, 12)
