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
        self.deck = []
        self.cardDistribution = {
            self.commonSuit: 12, 
            self.goalSuit: 8,     
        }

        def build_deck(self):
            for suit, count in self.cardDistribution.items():
                for _ in range(count):
                    self.deck.append(suit)
        
            for suit in Suit:
                if suit not in self.cardDistribution:
                    self.card_distribution[suit] = 10

