# Jothan Kelepolo
# 010.1
# 9/1/2020

import random
import os

while True:
    
    alphaChars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    numChars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    symbolChars = ["!", "@", "#", "$", "%","&", "?"]


    password = ""

    for i in range(0,random.randint(8,30)):
        choice = random.randint(1,3)
        if choice == 1:
            password = password + alphaChars[random.randint(0,len(alphaChars)-1)]
        elif choice == 2:
            password = password + numChars[random.randint(0,len(numChars)-1)]
        elif choice == 3:
            password = password + symbolChars[random.randint(0,len(symbolChars)-1)]


    print("Password: " + password)

    q = input("Enter to generate new password")

    if q == "q":
        break
    else:
        os.system("cls")
