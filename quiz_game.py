print("Welcome to my Quiz!")

player = input("Do you want to play?\t")
score = 0

if player.lower() != "yes": #.lower is a method to change the text to lower case
    quit()

question = input("What does RAM stand for?\t").lower()
if question == "random acces memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("What does BMW stand for?\t").lower()
if question == "Bavarian Engine Works":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("What does CPU stand for?\t").lower()
if question == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("1kg of gold is lighter than 1kg of feathers?\t")
if question.lower() == "no":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("What does GPU stand for?\t")
if question.lower == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You're score is: " + str(score))     #str() convert to string, because you can't add string to integer
                                            #"text" + number is not possible 
print("You got " + str((score / 5) * 100) + "%" + " done.")