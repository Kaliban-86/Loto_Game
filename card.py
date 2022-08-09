import random
import collections


class Card:

    def __init__(self):
        self.card_values = []
        self.card_name = ''

    def create_cards(self, name):
        while len(self.card_values) != 15:
            num = str(random.randint(1, 90))
            if num not in self.card_values:
                self.card_values.append(num)

        self.card_name = name

    def cross_out(self, num):
        if num in self.card_values:
            self.card_values[self.card_values.index(num)] = '--'

    def __str__(self):
        split_len = 11
        if len(self.card_name) < 8:
            split_len = 12

        first_str = str('-' * split_len + self.card_name + '-' * split_len)
        second_str = str(self.card_values[:5])
        tr_str = str(self.card_values[5:10])
        for_str = str(self.card_values[10:])
        fiv_str = str('--' * 15)
        return first_str + '\n' + second_str + '\n' + tr_str + '\n' + for_str + '\n' + fiv_str

    def __eq__(self, other):
        return collections.Counter(self.card_values) == collections.Counter(other.card_values)
