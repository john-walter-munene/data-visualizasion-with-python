from random import randint

class Die():
    """A class representing a single die"""
    
    def __init__(self, num_sides=6):
        """Assume a 6 sided die"""
        self.num_sides = num_sides
        
    def roll(self):
        """Retun a random value between 1 and the number of sides"""
        return randint(1, self.num_sides)
    
    