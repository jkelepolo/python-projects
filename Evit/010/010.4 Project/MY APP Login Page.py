# Jothan Kelepolo
# 010.4
# 9/3/2002

import os
import pickle
import os.path
from os import path


users = {}
if path.exists("data.pickle"):
    
    with open('data.pickle', 'rb') as handle:
        users = pickle.load(handle)

while True:
    name = input("Please enter your full name\n")
    pin = input("Enter Pin\n")

    ID = 0
    loggedIn = False



    for i in range(0,len(users)):
        if users[i]["name"].lower() == name.lower() and pin == users[i]["pin"]:
            ID = i
            loggedIn = True
            break
        
    if loggedIn == True:
        os.system("cls")
        print("Welcome " + users[ID]["name"]+"!")
        print("ID: "+ str(ID))
        print("Position: " + users[ID]["position"])
        print("Notes: " + users[ID]["notes"])

    else:
        os.system("cls")
        print("Wrong name or pin number")
        y = input("Create new user?\ny/n\n")
        if y == "y":
            os.system("cls")
            update = {len(users): {"name": input("Please enter your full name\n"), "pin": input("Enter your desired pin\n"), "notes": input("Enter a note about yourself\n"), "position": input("What is your company position?\n")}}
            for i in range(0,len(users)):
                if update[len(users)]["name"].lower() == users[i]["name"].lower():
                    print("\n\nName already taken.. Please try again.")
                    update = {}
            users.update(update)
            with open('data.pickle', 'wb') as handle:
                pickle.dump(users, handle, protocol=pickle.HIGHEST_PROTOCOL)

    q = input("\nPress enter to return to login screen\n(or 'q' to quit)\n")

    if q == "q":
        break
    else:
        os.system("cls")
