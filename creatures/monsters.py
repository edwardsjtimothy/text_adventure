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
crumblingSkeleton = Skeleton("Crumbling Skeleton", 3, 7)
giantSkeleton = Skeleton("Giant Skeleton", 10, 12)
