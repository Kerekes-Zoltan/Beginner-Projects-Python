name = input("Type your name: ")
print("Welcome", name, "to the adventure!")

question = input("You are on the road that has come to an end, there is left and there is right, which way do you want to go? ").lower()

if question == "left":
    question = input("You came accross a river, what do you want to do? Walk around the river of swim accross?").lower()
    if question == "swim":
        question = input("You swim accross so you die because you can't swim!").lower()
    elif question == "walk":
        print("You walked for many miles till you come accross to a beautiful girl, THE END!")
    else: 
        print("The answer is incorrect, please try again!")
elif question == "right":
    question = input("You come accross to a bridge, it looks dangerous, continue? (cross/back)").lower()
    if question == "back":
        question = input("You got lost. GAME OVER!").lower()
    elif question == "cross":
        print("You win!")
    else: 
        print("The answer is incorrect, please try again!")
else:
    print("The answer is incorrect, please try again!")