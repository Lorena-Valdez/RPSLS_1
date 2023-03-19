from player import Player
import random
from time import sleep
class Human(Player):

    def __init__(self,name):
        super().__init__()
        self.name = name

    def choose_move (self):
        gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
        sleep (1)
        print (f"{self.name} has picked {gesture_list[int(self.chosen_gesture)]}")

    def choose_move (number):
        if number == 0:
            return "Rock"
        elif number == 1:
            return "Paper"
        elif number == 2:
            return "Scissors"
        elif number == 3:
            return "Lizard"
        elif number == 4:
            return "Spock"
        else:
            return "Try again"
        
        # CHILD CLASS