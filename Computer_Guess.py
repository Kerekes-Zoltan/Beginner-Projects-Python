import random

def computer_guess(x):
    lower = 1
    higher = x
    feedback = ''
    while feedback != 'c':
        # if lower != higher:
        #     guess = random.randint(lower, higher)
        # else:
        #     guess = lower
        #line below is nicer the if statement
        guess = random.randint(lower, higher) if lower != higher else lower
        feedback = input(f"Is {guess} too High (H), too Low (L), or correct (C)").lower()
        if feedback == "h":
            higher = guess - 1
        elif feedback == "l":
            lower = guess - 1
    print(f"Pc guessed your number {guess}.")

computer_guess(5)
