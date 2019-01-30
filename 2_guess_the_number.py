import random

class Guess:
    """
        This is the class to get input number and compare random number and input number
    """
    def __init__(self, random_number):
        self.random_number = random_number
    
    """
        Takes input from user and checks whether it is integer and is between 1 and 10
    """
    def input_number(self):
        number = input("Enter a digit number between 1 and 10:\n")
        while number.isdigit() == False:
            number = input("Enter a digit number between 1 and 10:\n")
        while int(number)<1 or int(number)>10:
            number = input("Enter a digit number between 1 and 10:\n")
        return int(number)
    
    """
        Checks the difference between random number and input number and gives result whether
        the input number matches or is higher or is lower than generated random number
    """
    def difference_number(self,random_number, input_number):
        if random_number == input_number:
            print("Your guess is correct.")
        elif random_number > input_number:
            print("Your guess is incorrect and is lower than the generated number.")
        else:
            print("Your guess is incorrect and is higher than the generated nunmber.")
            
    def compare_number(self):
        input_number = self.input_number()
        self.difference_number(self.random_number, input_number)


# Generates random number between 1 and 10
random_number = random.randint(1,10)
g1 = Guess(random_number)
g1.compare_number()

        