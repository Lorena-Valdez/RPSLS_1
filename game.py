from ai import AI
from player import Player
from human import Human

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

    def play_game (self):
        while self.player_one.player_score <2 and self.player_two.player_score <2:
            self.player_one.chosen_move()
            self.player_two.chosen_move ()
            self.compare_moves()
            self.display_winner()

        #     self.compare_moves()
    def compare_moves (self):
        if self.player_one.chosen_move == self.player_two.chosen_move:
                print (f"You both chose {self.player_one.chosen_move}. Try again!")

        elif self.player_one.chosen_move == self.player_one.gestures[0] and (self.player_two.chosen_move == self.player_two.gestures[2] or self.player_two.chosen_move == self.player_two.gestures[3]):
            self.player_one.score += 1
        print (f"{self.player_one.chosen_move}{self.player_one.name} gets the point!")
        print(f"{self.player_one.name}'s move of {self.player_one.chosen_move} beat {self.player_two.name}'s {self.player_two.chosen_move}!")




        # if  self.player_one.chosen_move == 0:
        #     if self.player_two.chosen_move == 1:
        #         print ("Paper Covers Rock! {self.player_two.name} wins!")

        # if  self.player_one.chosen_move == 0:
        #     if self.player_two.chosen_move == 2:
        #         print ("Rock crushes Scissors. {self.player_one.name} wins!")

        # if  self.player_one.chosen_move == 0:
        #     if self.player_two.chosen_move == 3:
        #         print ("Rock crushes Lizard. {self.player_one.name} wins!")

        # if  self.player_one.chosen_move == 0:
        #     if self.player_two.chosen_move == 4:
        #         print ("Spock vaporizes Rock. {self.player_two.name} wins!")

        # if  self.player_one.chosen_move == 1:
        #     if self.player_two.chosen_move == 0:
        #         print ("Paper Covers Rock! {self.player_one.name} wins!") 

        # if  self.player_one.chosen_move == 1:
        #     if self.player_two.chosen_move == 2:
        #         print ("Paper Covers Rock! {self.player_one.name} wins!")        
        #     self.display_winner()
    
    def play_game (self):
        self.display_title
        self.game_rules

    

        def display_winner (self):
            print (f"{self.winner} wins the set!")
        
    # if 

        # loop back to start if selection is anything other than 0-4


    def play_mode (self):
        print ("How many players? Press 1 or 2")
        self.play_mode = input ("")

        if self.play_mode == "1":
            print ("You will play against Roboticus Maximus")
            self.player_one = Human ()
            self.player_two = AI("Roboticus Maximus")
        
        if self.play_mode =="2":
            print ("You have chosen to play another person")
            self.player_one = Human()
            self.player_two = Human()
        
        else:
            print ("That is not a valid selection. Please choose 1 or 2.")
            self.play_mode ()


# write loop to return to top if 0-4 selection not made. make sure that this is for human player ONLY
# Three wins determine a winner of that match
# Declare winner