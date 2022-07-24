import random


def show_card(card, name):
    split_len = 10
    if len(name) < 8:
        split_len = 11
    print('-' * split_len, name, '-' * split_len)
    print(card[:5])
    print(card[5:10])
    print(card[10:])
    print('--' * 15)


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

