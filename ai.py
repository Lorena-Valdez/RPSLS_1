from player import Player
import random
from time import sleep
class AI(Player):

    def __init__(self,name):
        super().__init__()
        self.score = 0
        self.name = name

    def choose_move (self):
        self.chosen_move = str(random.rantint (0,4))
        move_list = ["Rock","Paper", "Scissors","Lizard","Spock"]
        sleep (1)
        print (f"{self.name} has picked {move_list[int(self.chosen_move)]}")

# CHILD CLASS

# wmust have things in common from parent  class
# self.random_choice = random_choice only in ai class