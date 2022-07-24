import random


class Pouch:

    def __init__(self):
        self.pouch = [barrel_num for barrel_num in range(1, 91)]

    def get_barrel(self):
        barrel_index = random.randint(0, len(self.pouch))
        barrel_num = self.pouch.pop(barrel_index-1)
        return barrel_num

