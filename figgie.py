import random
from Game import Game

if __name__ == '__main__':
    
    ## CUSTOM SETTINGS
    # num_players = int(input("Enter the number of players. (typically 4-5) "))
    # num_bots = int(input(f"How many of the {num_players} are bots? "))
    # while (num_bots > num_players):
    #     num_bots = int(input(f"The number of bots cannot exceed {num_players}. Pick a smalelr number. "))
    # number_of_rounds = int(input("Enter the number of rounds to play. "))
    # starting_balance = int(input("Enter the starting balance for each player. "))
    # starting_pot = int(input("Enter the pot for the match. "))
    
    # PREDEFINED SETTINGS
    num_players = 4
    num_bots = 2 # must be [0, num_players]
    number_of_rounds = random.randint(5,20)
    starting_balance = 350
    pot = 200

    player_names = ["Player"+str(i) for i in range(num_players-num_bots)]

    # start game w/ defined variables
    game = Game(num_players, player_names, number_of_rounds, starting_balance, pot)
    
    # play game
    game.play_game()
