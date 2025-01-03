import random
from Card import Card

suits = ["hearts", "diamonds", "clubs", "spades"]

class Pack:
    def __init__(self, common_suit):
        unused_suits = suits.copy()

        unused_suits.remove(common_suit)
        random_suit = random.choice(unused_suits)
        unused_suits.remove(random_suit)

        # make 12 common suits, 8 and 10 (x2) other suit
        self.cards = [Card(common_suit) for _ in range(12)] + \
                     [Card(random_suit) for _ in range(8)] + \
                     [Card(suit) for suit in unused_suits for _ in range(10)]
        self.shuffle()

        self.size = 40

    def get_size(self):
        return self.size

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        self.size -= 1
        return self.cards.pop()
