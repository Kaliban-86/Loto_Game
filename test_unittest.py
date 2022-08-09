import unittest
from card import Card
from pouch_with_barrels import Pouch
from player import Player


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card()

    def test_init(self):
        self.assertEqual(self.card.card_values, [])
        self.assertEqual(self.card.card_name, '')

    def test_create_card(self):
        self.card.create_cards('My card')
        self.assertEqual(self.card.card_name, 'My card')
        self.assertEqual(len(self.card.card_values), 15)
        for i in range(15):
            self.assertTrue((int(self.card.card_values[i]) >= 1) & (int(self.card.card_values[i]) <= 90))

    def test_cross_out(self):
        self.card.create_cards('test card')
        self.card.card_values[0] = 7
        self.card.cross_out(7)
        self.assertEqual(self.card.card_values[0], '--')

    def test_magic_eq(self):
        self.card.create_cards('test_1')
        test_2 = Card()
        test_2.create_cards('test_2')
        self.assertEqual(self.card.card_values == test_2.card_values, False)



class TestPouch(unittest.TestCase):

    def setUp(self):
        self.pouch = Pouch()

    def test_init(self):
        self.assertEqual(len(self.pouch.pouch), 90)
        for i in range(0, 90):
            self.assertEqual(self.pouch.pouch[i], i + 1)

    def test_get_barrels(self):

        for i in range(90):
            barrel_num = self.pouch.get_barrel()
            self.assertTrue((barrel_num >= 1) & (barrel_num <= 90))

        self.assertEqual(len(self.pouch.pouch), 0)


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player('player name')

    def test_init(self):
        self.assertEqual(self.player.name, 'player name')
        self.assertEqual(self.player.cross_count, 0)

    def test_counting_win(self):
        self.player.counting_win()
        self.assertEqual(self.player.cross_count, 1)

    def test_magic_eq(self):
        player_2 = Player('player_2')
        self.assertEqual(self.player == player_2, False)
