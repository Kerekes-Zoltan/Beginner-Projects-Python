#string concatenation (aka how to put string togheter)
#we want to create a string that says "subscribe to ______"

# sourcery skip: use-fstring-for-formatting
youtuber = "your favorite youtuber" #example of string variable

#a few ways to do this
print(f"subscribe to {youtuber}")
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")

#<-----Example----->
adj = input("Adjective: ")
verb1 = input("Verb1: ")
verb2 = input("Verb2: ")
famous_person = input("Famous Person: ")
madlib = f"Working as a developer is so {adj}! Makes me happy all the time, because I love to {verb1}. Go to the Gym to stay healthy and {verb2} like The {famous_person}!"

print(madlib)