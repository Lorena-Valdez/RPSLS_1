from player import Player

import random
from time import sleep

class Human(Player):
    def __init__(self):
        super().__init__(input ("Please Enter Name "))


    def choose_move (self):

        print ("Choose (0) for Rock, (1) for Paper, (2) for Scissors, (3) for Lizard and (4) for Spock")
       
        # user_input = int (input ("Choose your move!"))
        user_input = int (input (f"{self.name} choose your move!"))
        self.chosen_move = self.gestures[user_input]
        print (f"{self.name} has picked {self.chosen_move}")

        
