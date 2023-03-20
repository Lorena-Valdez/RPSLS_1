from player import Player
import random
from time import sleep

class AI(Player):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.name = "Roboticus Maximus"

    def choose_move (self):
        self.chosen_move = random.choice(self.gestures)
        sleep (1)
        print (f"Roboticus Maximus has picked (self.chosen_move)")


# must have things in common from parent  class
# self.random_choice = random_choice only in ai class