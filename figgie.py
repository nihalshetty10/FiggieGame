import random
from enum import Enum



class Suit(Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

opposite_suit = {
    Suit.HEARTS: Suit.DIAMONDS,
    Suit.DIAMONDS: Suit.HEARTS,
    Suit.CLUBS: Suit.SPADES,
    Suit.SPADES: Suit.CLUBS
}

class figgie:
    def __init__(self, rounds):
        self.rounds = rounds
        self.goalSuit = random.choice(list(Suit))
        self.commonSuit = opposite_suit[self.goalSuit]
        self.deck

