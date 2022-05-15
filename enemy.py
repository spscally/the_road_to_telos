import random

class Enemy():

    def __init__(self, level):
        self.max_health = 10 * level + random.randint(0, level * 2)
        self.health = self.max_health
        self.attack = level
        self.luck = 1