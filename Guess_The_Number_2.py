#Guess the number that the Computer generated

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 #variable can have the 0 value because the range is between 1 and x
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Guess again. Too Low!")
        elif guess > random_number:
            print("Guess again. Too High!")
    
    print("Congratulation. You win! The number was {}.".format(guess))

guess(5)