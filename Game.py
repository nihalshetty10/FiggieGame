from Pack import Pack
from Player import Human, Bot
import random
import heapq

suits = ["hearts", "diamonds", "clubs", "spades"]

opposite_suit = {
    "hearts" : "diamonds",
    "diamonds" : "hearts",
    "clubs" : "spades",
    "spades" : "clubs"
}

opposite_action = {
    "bid" : "ask",
    "ask" : "bid"
}

class Game:
    def __init__(self, num_players, player_names, rounds, starting_balance):
        self.players = [Human(name, starting_balance) for name in player_names]
        self.players += [Bot("Bot"+str(i), starting_balance) for i in range(num_players - len(self.players))]

        self.rounds = rounds
        self.goalSuit = random.choice(suits)
        self.commonSuit = opposite_suit[self.goalSuit]

        self.pack = Pack(self.goalSuit, self.commonSuit)

        self.round_actions = []
        self.round_transactions = []
        self.market = {
            "hearts": {"bid": [], "ask": []},
            "diamonds": {"bid": [], "ask": []},
            "clubs": {"bid": [], "ask": []},
            "spades": {"bid": [], "ask": []}
        }

    def play_game(self):
        # deal pack to players
        while self.pack.get_size() != 0:
            for player in self.players:
                player.receive_card(self.pack.deal_card().get_suit())

        # display hand for each player
        self.display_hands()

        # self.rounds =  amount of rounds 
        for round in range(self.rounds):
            print(f"ROUND {round + 1}")
            self.play_round()
            self.display_actions()
            self.display_update()

        print("Game finished!")

    def play_round(self):
        for player in self.players:
            action, suit, price = player.decide_action()
            self.process_actions(action, suit, price, player)

    def process_actions(self, action, suit, price, player):
        # add action to list for round summary
        if action == "pass":
            self.round_actions.append(f"{player.get_name()} passed.")
        else:
            self.round_actions.append(f"{player.get_name()} chose to {action} {price} dollars for a card of {suit}.")

        # complete possible transactions
        if action != "pass" and len(self.market[suit][opposite_action[action]]) == 0:
            pass
        elif (action == "bid") and (int(self.market[suit]["ask"][0][0]) <= int(price)):
            ask_price, seller = heapq.heappop(self.market[suit]["ask"])
            player.receive_card(suit)
            player.update_balance(-ask_price) # remove from balance
            seller.remove_card(suit)
            seller.update_balance(ask_price) # add to balance
            self.round_transactions.append(f"TRANSACTION: {player.get_name()} bought a card of {suit} from {seller.get_name()} for {ask_price}.")
            return
        elif (action == "ask") and (-int(self.market[suit]["bid"][0][0]) >= int(price)):
            bid_price, buyer = heapq.heappop(self.market[suit]["bid"])
            player.remove_card(suit)
            player.update_balance(-bid_price) # add to balance
            buyer.receive_card(suit)
            buyer.update_balance(bid_price) # remove from balance
            self.round_transactions.append(f"TRANSACTION: {buyer.get_name()} bought a card of {suit} from {player.get_name()} for {-bid_price}.")
            return

        # if no transaction, add action to market
        if action == "bid":
            # create a max-heap of bids
            heapq.heappush(self.market[suit]["bid"], (-int(price), player))
        if action == "ask":
            # crate a min-heap of asks
            heapq.heappush(self.market[suit]["ask"], (int(price), player))

    def display_hands(self):
        print("Hands of each player:")
        for player in self.players:
            print(f"{player.get_name()}: {player.get_hand()}")
        print("\n")

    def display_actions(self):
        print(f"=============================\nROUND SUMMARY")

        for recorded_action in self.round_actions:
            print(recorded_action)
        print("\n")  # spacing

        if len(self.round_transactions) > 0:
            for recoreded_transaction in self.round_transactions:
                print(recoreded_transaction)
        else:
            print("No transaction completed")

        self.round_actions.clear()
        self.round_transactions.clear()


    def display_update(self):
        print(f"=============================\nROUND FINISHED")
        for player in self.players:
            player.display_status()
        print("=============================\n")