from Game import Game

if __name__ == '__main__':
    
    ## CUSTOM SETTINGS
    # num_players = int(input("How many players are there? (typically 4-5) "))
    # num_bots = int(input(f"How many of the {num_players} should be bots? "))
    # while (num_bots > num_players):
    #     num_bots = int(input(f"The number of bots cannot exceed {num_players}. Pick a smalelr number. "))
    # number_of_rounds = int(input("How many rounds do you want to play? "))
    # starting_balance = int(input("What do should the starting balance for each player be? "))
    
    # PREDEFINED SETTINGS
    num_players = 4
    num_bots = 2 # must be [0, num_players]
    number_of_rounds = 20
    starting_balance = 350

    player_names = ["Player"+str(i) for i in range(num_players-num_bots)]

    # start game w/ defined variables
    game = Game(num_players, player_names, number_of_rounds, starting_balance)
    
    # play game
    game.play_game()
