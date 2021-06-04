# Jothan Kelepolo
# 10.4 Shared
# 9/4/2020

import pickle
import os
import os.path
from os import path

users = {}
if path.exists("data.ini"): # Checks if path exists to avoid trying to open a non-existant file
    
    with open('data.ini', 'rb') as handle: # load data file
        users = pickle.load(handle)



while True:
    
    if "admin" not in users: # Checks if there is an existing admin account
        print("Warning 'admin' account not registered please register it")
        input("Enter to continue")
    
    os.system("cls")
    choice = input("1. Login\n2. Register\n3. Quit\n")
    os.system("cls")
    
    if choice == "1":
        user = input("Login\n--------\nUsername: ")
        password = input("Password: ")

        if user.lower() in users and users[user.lower()] == password:  # Checks if entered username is in the dictionary and if it matches a password
            print("\nSuccessfully logged in as "+str(user))
            if user.lower() == "admin": # If the user name is equal to the lower case of 'admin' then log user in as an admin
                os.system("cls")
                print("\nYou are logged in as an ADMIN\n\n{'username': 'password'}\n")
                print(str(users)) # prints the dictionary as a string
        elif user.lower() in users and users[user.lower()] != password: 
            print("\nWrong password!") # checks if entered username is in dictionary and checks if the password is wrong
        else:
            print("Account does not exist please register it") # if it gets this far the username does not exist in the dictionary, prompt user to register
        input("Enter to continue")


    elif choice == "2":
        user = input("Register\n--------\nUsername: ").lower()
        password = input("Password: ")

        if user in users: # checks if username already exists in the dictionary
            print("User already exists! Please try again.")
        elif user not in users: # if username is not in the list update the list
            print("User successfully added!")
            update = {user:password}
            users.update(update)
            with open('data.ini', 'wb') as handle: #pickle the data and save
                pickle.dump(users, handle, protocol=pickle.HIGHEST_PROTOCOL)
            input("Enter to continue")

            
    elif choice == "3":
        break
    os.system("cls")
