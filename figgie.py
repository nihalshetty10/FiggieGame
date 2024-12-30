from Game import Game
​
if __name__ == '__main__':
    # currently predefined settings set here
    player_names = ['Player1', 'Player2', 'Player3', 'Player4']
    number_of_rounds = random.randint(10, 20)
    starting_balance = 350
​
    # start game w/ defined variables
    game = Game(player_names, number_of_rounds, starting_balance)
    
    # play game
    game.play_game()
