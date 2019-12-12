#random number module
import random

class Skeleton:
    name: ""
    health: 0
    maxHealth: 0
    stamina: 0
    maxStamina: 0

    def __init__(self, me, hp, st):
        self.name = me 
        self.health = hp + random.randrange(5, 10)
        self.maxHealth = self.health
        self.stamina = st + random.randrange(5, 10)
        self.maxStamina = self.stamina

    def staminaRegen(self):
        if self.stamina < self.maxStamina:
            self.stamina += random.randrange(1, 3)
            if self.stamina > self.maxStamina:
                self.stamina = self.maxStamina

#basic attack
    def bludgeon(self, target):
        hit = random.randrange(1, 21)
        dmg = 1 + random.randrange(1, 3)
        crit = dmg * 2

        #stamina regen
        self.staminaRegen()

        if hit > 12:
            target.health -= dmg
            print(f"You took {dmg} damage!")
        elif hit == 20: 
            target.health -= crit
            print(f"Critical strike! You took {dmg} damage!")
        elif hit < 13:
            print("Your enemy's attack missed!")

#stronger attack
    def lumberingStrike(self, target):
        hit = random.randrange(1, 21)
        dmg = 2 + random.randrange(2, 4)
        crit = dmg * 2

        #stamina regen
        self.staminaRegen()

        if self.stamina < 15:
            print("Insufficient stamina!")
            return
        elif self.stamina >= 15:
            self.stamina -= 15

        if hit > 15:
            target.health -= dmg
            print(f"You took {dmg} damage!")
        elif hit == 20: 
            target.health -= crit
            print(f"Critical strike! You took {dmg} damage!")
        elif hit < 16:
            print("Your enemy's attack missed!")

#chance at collapsing at low health
    def collapse(self):
            if self.health < 7:
                collapse = random.randrange(1, 21)

                if collapse < 10:
                    self.health = 0 
                    print("The necrotic energy animating your target dispates with a sigh; it collapses with a dry clatter of falling bones...")

#random ability selector
    def abilitySelect(self, target):
        whichAbility = random.randrange(1,7)
        if whichAbility <= 3:
            self.bludgeon(target)
        elif whichAbility <= 5:
            self.lumberingStrike(target)
        elif whichAbility == 6:
            self.collapse()







ancientSkeleton = Skeleton("Ancient Skeleton", 5, 10)
crumblingSkeleton = Skeleton("Crumbling Skeleton", 3, 7)
giantSkeleton = Skeleton("Giant Skeleton", 10, 12)
