import random

player_w = 0
pc_w = 0

options = ["rock", "paper", "scissors"]

while True:
    player_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if player_input == "q":
        break

    if player_input not in ["rock", "paper", "scissors"]: #it is a list, I want to check what is typed to be in the list
        continue

    number = random.randint(0,2)
    #rock = 0, paper = 1, scissors: 2

    pc_pick = options[number]

    print("Computer picked", pc_pick + ".")

    if player_input == 'rock' and pc_pick == "scissors":
        print("Player won!")
        player_w += 1

    elif player_input == 'paper' and pc_pick == "rock":
        print("Player won!")
        player_w += 1

    elif player_input == 'scissors' and pc_pick == "paper":
        print("Player won!")
        player_w += 1

    else:
        print("You lost!")
        pc_w += 1

print("Player won", player_w, "times")
print("Computer won", pc_w, "times")
print("Goodbye!")