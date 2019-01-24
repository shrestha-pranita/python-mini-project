import random

class Dice:
    """
        This is the class for dice range calculation
    """
    
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        
    def random_number(self):
        print("The dice number is: ")
        print(random.randint(self.minimum, self.maximum))

            
answer = "yes"        
while answer == "yes":
    d1 = Dice(1, 6)
    d1.random_number()
    answer = input("Roll the dice again: Yes or No\n")
    answer = answer.lower()
    while answer != "yes" and answer != "no":
        answer = input("Please input Yes or No. Roll the dice again: Yes or No\n")