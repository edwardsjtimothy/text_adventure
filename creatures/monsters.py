#random number module
import random

class Skeleton:
    name: ""
    health: 0
    stamina: 0

    def __init__(self, me, hp, st):
        self.name = me 
        self.health = hp + random.randrange(5, 10)
        self.stamina = st + random.randrange(5, 10)




ancientSkeleton = Skeleton("Ancient Skeleton", 5, 10)

