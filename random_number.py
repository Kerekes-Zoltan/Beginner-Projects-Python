from curses.ascii import isdigit
import random #This is a module

#randrange does not include the stop (-5, 5), does not include 5
#randint does include the last number (-5, 5), does include 5

maxim_range = input("Type a number: ")  #the input will be "25" so int() changes to string -> int("25") => 25
score = 0

if maxim_range.isdigit():   #isdigit confirms if the text is a number
    maxim_range = int(maxim_range)

    if maxim_range <= 0:
        print("NUmber is larger than 0")
        quit()
else:
    quit()

number = random.randrange(maxim_range + 1)

while True:
    score += 1
    player_guess = input("Make a guess: ")
    if player_guess.isdigit():
        player_guess = int(player_guess)
    else:
        print("Type a number next time!")
        continue #This will send us back to the top until the input is a number

    if player_guess == number:
        print("It is correct!")
        break
    
    elif player_guess > number:
        print("You were above the number")
    else:
        print("You were below the number")

print("You made it in ", score, "guesses")