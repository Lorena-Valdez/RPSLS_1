class Game:
    # def __init__(self):
    #     self.

    def run_game (self):
        self.display_title ()
        self.game_rules()
        self.play_mode ()
        self.play_game ()
        self.display_winner()

    def display_title (self):
        print("\nWelcome to Rock, Paper, Scissors, Lizard, Spock \n")
        from time import sleep
    
    def game_rules (self):
        print ("""    The rules are simple:\n
    Scissors cuts Paper \n
    Paper covers Rock \n
    Rock crushes Lizard \n
    Lizard poisons Spock \n
    Spock smashes Scissors \n
    Scissors decapitates Lizard \n
    Lizard eats Paper \n
    Paper disproves Spock \n
    Spock vaporizes Rock \n
    and of course, \n
    Rock crushes Scissors""")
        from time import sleep

    def play_mode (self):
        while self.player_one.player_score <2 and self.player_two.player_score <2:
            self.player_one.chosen_move()
            self.player_two.chosen_move ()
            self.compare_moves()
            self.display_winner()

        while self.play_mode:
            self.player_one.player_score <2 and ai.player <2:
            self.compare_moves()
            self.display_winner()
    
    def play_game (self):
        
    

    def display_winner (self):
        print (f"{self.winner} wins the set!")
        
    
        # loop back to start if selection is anything other than 0-4

    #  write input for player(s),


# write loop to return to top if 0-4 selection not made. make sure that this is for human player ONLY
# Three wins determine a winner of that match
# Declare winner