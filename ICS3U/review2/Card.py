import random

class Card:
    def __init__(self):
        self.set_suit()
        self.set_card_no()

    def set_suit(self):
        self.suit = random.choice(["C", "D", "H", "S"])

    def set_card_no(self):
        self.card_no = random.randint(0, 12)

    def draw_card(self):
        self.set_suit()
        self.set_card_no()

    def get_card_suit(self):
        return self.suit

    def get_card_value(self):
        card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        return card_values[self.card_no]

    def get_card_name(self):
        card_names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        return card_names[self.card_no]

