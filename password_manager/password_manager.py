from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key() + master_password.encode()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()        #the output reads the \n so rstrip() deletes that last charage return
            user, passw = data.split("|") #this will split the data in two, user and password
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account name: ")
    password = input("Password: ")

    with open('password.txt', 'a') as f: #you can use file = open... but with this method the process will not close the file and so you need to close it manually
        f.write(name + " | " + fer.encrypt(password.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones? (view/add)\t").lower()

    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue