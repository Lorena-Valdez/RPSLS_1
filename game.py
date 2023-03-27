from ai import AI
from player import Player
from human import Human

class Game:
    def __init__(self):
        pass

    def run_game (self):
        self.display_title()
        self.game_rules()
        self.play_mode()
        self.play_game()
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
        print ("How many players? Press 1 or 2")
        user_input = input ("")

        if user_input == "1":
            self.player_one = Human()
            print ("You will play against Roboticus Maximus")
            self.player_two = AI()
        elif user_input =="2":
            print ("You have chosen to play another person")
            self.player_one = Human()
            self.player_two = Human()     
        else:
            print ("That is not a valid selection. Please choose 1 or 2.")
            user_input= input("")

    def play_game (self):
        while self.player_one.score <2 and self.player_two.score <2:
            self.player_one.choose_move()
            self.player_two.choose_move()
            self.compare_moves()
        self.display_winner()

    
    def compare_moves (self):
        if self.player_one.chosen_move == self.player_two.chosen_move:
                print (f"You both chose {self.player_one.chosen_move}. Try again!")

        elif self.player_one.chosen_move == self.player_one.gestures[0] and (self.player_two.chosen_move == self.player_two.gestures[2] or self.player_two.chosen_move == self.player_two.gestures[3]):
            self.player_one.score += 1
            self.roundMessage(self.player_one,self.player_two)

        elif self.player_one.chosen_move == self.player_one.gestures[1] and (self.player_two.chosen_move == self.player_two.gestures[0] or self.player_two.chosen_move == self.player_two.gestures[4]):
            self.player_one.score += 1
            self.roundMessage(self.player_one,self.player_two)
        
        elif self.player_one.chosen_move == self.player_one.gestures[2] and (self.player_two.chosen_move == self.player_two.gestures[1] or self.player_two.chosen_move == self.player_two.gestures[3]):
            self.player_one.score += 1
            self.roundMessage(self.player_one,self.player_two)
        
        elif self.player_one.chosen_move == self.player_one.gestures[3] and (self.player_two.chosen_move == self.player_two.gestures[1] or self.player_two.chosen_move == self.player_two.gestures[4]):
            self.player_one.score += 1
            self.roundMessage(self.player_one,self.player_two)

        elif self.player_one.chosen_move == self.player_one.gestures[4] and (self.player_two.chosen_move == self.player_two.gestures[0] or self.player_two.chosen_move == self.player_two.gestures[2]):
            self.player_one.score += 1
            self.roundMessage(self.player_one,self.player_two)

        elif self.player_one.chosen_move == self.player_one.gestures[0] and (self.player_two.chosen_move == self.player_two.gestures[1] or self.player_two.chosen_move == self.player_two.gestures[4]):
            self.player_two.score += 1
            self.roundMessage(self.player_two,self.player_one)

        elif self.player_one.chosen_move == self.player_one.gestures[1] and (self.player_two.chosen_move == self.player_two.gestures[2] or self.player_two.chosen_move == self.player_two.gestures[3]):
            self.player_two.score += 1
            self.roundMessage(self.player_two,self.player_one)
       
        elif self.player_one.chosen_move == self.player_one.gestures[2] and (self.player_two.chosen_move == self.player_two.gestures[0] or self.player_two.chosen_move == self.player_two.gestures[4]):
            self.player_two.score += 1
            self.roundMessage(self.player_two,self.player_one)    
       
        elif self.player_one.chosen_move == self.player_one.gestures[3] and (self.player_two.chosen_move == self.player_two.gestures[0] or self.player_two.chosen_move == self.player_two.gestures[2]):
            self.player_two.score += 1
            self.roundMessage(self.player_two,self.player_one)
       
        elif self.player_one.chosen_move == self.player_one.gestures[4] and (self.player_two.chosen_move == self.player_two.gestures[1] or self.player_two.chosen_move == self.player_two.gestures[3]):
            self.player_two.score += 1
            self.roundMessage(self.player_two,self.player_one)
        # else:
        #     print ("That is not a valid gesture. Rock = 0, Paper = 1, Scissors = 2, Lizard = 3 and Spock = 4. Please choose a number between 0 and 4")
        #     self.gestures = input("")


    def roundMessage (self, winner, loser):
        print (f" {winner.name} gets the point! Their score is now {winner.score}")
        print(f"{winner.name}'s move of {winner.chosen_move} beats {loser.name}'s {loser.chosen_move}!")

        
    def display_winner (self):

        if self.player_one.score >= 2 :
            print (f"{self.player_one.name} wins the game!")
        elif self.player_two.score >= 2:
            print (f"{self.player_two.name} wins the game!")


# write loop to return to top if 0-4 selection not made. make sure that this is for human player ONLY
# Three wins determine a winner of that match
# Declare winner