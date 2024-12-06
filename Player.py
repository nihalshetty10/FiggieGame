import random

class Player:
    def __init__(self, name, starting_balance):
        self.name = name
        self.balance = starting_balance
        self.hand = {
            "hearts" : 0,
            "diamonds" : 0,
            "clubs" : 0,
            "spades" : 0
        }

    def display_status(self):
        print(f"{self.name}'s Balance: ${self.balance}")

    def receive_card(self, suit):
        self.hand[suit] += 1

    def remove_card(self, suit):
        self.hand[suit] -= 1

    def update_balance(self, price):
        self.balance += price

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance
    
    def get_hand(self):
        return self.hand

# create custom decision making for human vs bot
class Human(Player):
    def decide_action(self):
        # decide an action for turn
        picked_action = input(f"{self.name}: bid, ask, or pass? ")
        while picked_action.lower() not in ["bid", "ask", "pass"]:
            picked_action = input(f"{self.name}: bid, ask, or pass? ")

        # decide suit for action
        if (picked_action.lower() != "pass"):
            picked_suit = input(f"{self.name}: what suit would you like to {picked_action} for? ")
            while picked_suit.lower() not in ["hearts", "diamonds", "clubs", "spades"]:
                picked_suit = input(f"{self.name}: select either Hearts, Diamonds, Clubs, or Spades. ")

            while (picked_action.lower() == "ask") and (self.hand[picked_suit.lower()] == 0): # no card of given suit in hand
                input(f"{self.name}: no card of suit {picked_suit} found in your hand. Pick a new suit. ")

            # decide price for action
            picked_price = input(f"{self.name}: what price would you like to {picked_action} a {picked_suit} card for? ")
            while (picked_action.lower() == "bid") and (int(picked_price) > self.balance): # check validity of bid price
                input(f"{self.name}: insufficient funds. Your bid price exceeds your current balance of {self.balance}. Pick a lower bid price. ")

            # if action != pass    
            return picked_action, picked_suit, picked_price
        # if action == pass
        return picked_action, "", 0

class Bot(Player):
    def decide_action(self):
        picked_action = random.choice(["bid", "ask", "pass"])
        picked_suit = random.choice(["hearts", "diamonds", "clubs", "spades"])
        while (picked_action.lower() == "ask") and (self.hand[picked_suit.lower()]) == 0:
            picked_suit = random.choice(["hearts", "diamonds", "clubs", "spades"])
        picked_price = random.randint(1, self.balance//3)

        return picked_action, picked_suit, picked_price