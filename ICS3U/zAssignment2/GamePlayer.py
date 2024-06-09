"""
Robert
ICS3UO
GamePlayer.py
May 28

Class File that provides Game.py the neccessary variables and fucntions to support its code. 
"""
from random import randint

class GamePlayer():
    #initilize variables and their values upon instance creation 
    def __init__(self, low_range, high_range):
        self.low_range = low_range
        self.high_range = high_range
        self.move_value = 0
        self.wins = 0
    
    #Generate move value, by getting a random value between the low range and high range 
    def move(self):
        self.move_value = randint(self.low_range, self.high_range)

    #return the move value
    def get_move_value(self):
        return self.move_value

    #A win has been indicated, add to the instances tally of wins 
    def win(self): 
        self.wins += 1 

    #return the number of wins
    def get_wins(self):
        return self.wins