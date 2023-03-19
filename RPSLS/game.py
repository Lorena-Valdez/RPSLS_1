class Game:
    # def __init__(self):
    #     self.

    def run_game (self):
        self.display_title ()
        self.game_rules()
        self.display_winner()
        self.play_mode ()

    def display_title (self):
        print("\nWelcome to Rock, Paper, Scissors, Lizard, Spock \n")
        
    
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


    def play_mode (self):
        print ("Play against a person or AI? 1 for Person or 2 for AI")
        self.input =()  
        if self.play_mode == "1":
            self.use_ai = False
        if self.play_mode == "2":
            self.use_ai = True   

    def display_winner (self):
        print (f"{self.winner} wins the set!")
        
    
        # loop back to start if selection is anything other than 0-4
    

# write input for player(s),
# write loop to return to top if 0-4 selection not made. make sure that this is for human player ONLY
# write what each number means when selected. i.e You choose 1 "paper", 
# parent class, name, score, gesture list, and currently selected gesture.
# ai is diff by HOW they pick gestures
# human choose gesture and access gesture in game.py then we can have access to player moves and to compare the two. 
# Three wins determine a winner of that match
# Declare winner

# GITBASH then work on above