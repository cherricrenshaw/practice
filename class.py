import random

class NumberDie:
    def_init_(self, num_of_sides):
        self.number_of_sides=num_of_sides
        self.current_value=-1
        
def roll(self):
    self.current_value=random.randint(1,self.number_of_sides)
    
