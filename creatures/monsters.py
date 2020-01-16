#random number module
import random

class Skeleton:
    name: ""
    health: 0
    maxHealth: 0
    stamina: 0
    maxStamina: 0
    manueverCount: 0
    hit = 0
    dmg = 0
    crit = 0

    def __init__(self, me, hp, st):
        self.name = me 
        self.health = hp + random.randrange(5, 10)
        self.maxHealth = self.health
        self.stamina = st + random.randrange(5, 10)
        self.maxStamina = self.stamina
        self.maneuverCount = 0
        self.hit = 0
        self.dmg = 0
        self.crit = 0

    def staminaRegen(self):
        if self.stamina < self.maxStamina:
            self.stamina += random.randrange(1, 3)
            if self.stamina > self.maxStamina:
                self.stamina = self.maxStamina

    def maneuverTracker(self):
        if self.maneuverCount >= 4:
                self.maneuverCount = 3
        if self.maneuverCount == 1: 
            self.stamina += 15
            self.hit = random.randrange(16, 21)
            self.dmg = 5 + random.randrange(1, 3)
        elif self.maneuverCount == 2:
            self.stamina += 15
            self.hit = random.randrange(18, 21)
            self.dmg = 10 + random.randrange(5, 10)
        elif self.maneuverCount == 3:
            self.stamina += 15
            self.hit = 20
            self.dmg = 10 + random.randrange(15, 25)

#basic attack
    def bludgeon(self, target):
        self.hit = random.randrange(1, 21)
        self.dmg = 1 + random.randrange(1, 3)
        self.crit = self.dmg * 2

# tracking consecutive uses of Maneuver and increasing damage likelihood and output for each consecutive use.
        self.maneuverTracker()

        #stamina regen
        self.staminaRegen()

        if 12 < self.hit < 19:
            target.health -= self.dmg
            print(f"You took {self.dmg} damage!")
        elif self.hit == 20: 
            target.health -= self.crit
            print(f"Critical strike! You took {self.crit} damage!")
        elif self.hit < 13:
            print("Your enemy's attack missed!")

#stronger attack
    def lumberingStrike(self, target):
        self.hit = random.randrange(1, 21)
        self.dmg = 2 + random.randrange(2, 4)
        self.crit = self.dmg * 2
        
# tracking consecutive uses of Maneuver and increasing damage likelihood and output for each consecutive use.
        self.maneuverTracker()

        #stamina regen
        self.staminaRegen()


        if self.stamina < 15:
            print("Your foe is too exhausted to attack!")
            return
        elif self.stamina >= 15:
            self.stamina -= 15
            if 15 < self.hit < 19:
                target.health -= self.dmg
                print(f"You took {self.dmg} damage!")
            elif self.hit == 20: 
                target.health -= self.crit
                print(f"Critical strike! You took {self.crit} damage!")
            elif self.hit < 16:
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
targetDummy = Skeleton("Target Dummy", 200, 0)
miniDummy = Skeleton("Mini Dummy", 0, 0)
