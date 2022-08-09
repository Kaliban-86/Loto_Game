class Player:

    def __init__(self, name):
        self.name = name
        self.cross_count = 0

    def counting_win(self):
        self.cross_count += 1

    def __eq__(self, other):
        return self.name == other.name