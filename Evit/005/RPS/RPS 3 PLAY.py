# Jothan Kelepolo
# Project 5
# 8/18/2020
import sys

NameOne = input("Player 1:\n")
NameTwo = input("Player 2:\n")
NameThree = input("Player 3:\n")
while True:
    # ask for Rock Paper or Scissors
    print("\nRock > Scissors, Paper > Rock, Scissors > Paper")
    print(NameOne+":")
    PlayerOne = input("1. Rock \n2. Paper \n3. Scissors\n")
    
    print("\n"*100)

    print(NameTwo+":")
    PlayerTwo = input("1. Rock \n2. Paper \n3. Scissors\n")

    print("\n"*100)
    
    print(NameThree+":")
    PlayerThree = input("1. Rock \n2. Paper \n3. Scissors\n")

    #Rock Paper Scissors Grouping Player 1 and 2

    if PlayerOne == "1" and PlayerTwo == "2":
        print(NameTwo + " beat " + NameOne + " with Paper")
        input()
    elif PlayerOne == "2" and PlayerTwo == "1":
        print(NameOne + " beat " + NameTwo + " with Paper")
        input()

    if PlayerOne == "1" and PlayerTwo == "3":
        print(NameOne + " beat " + NameTwo + " with Rock")
        input()
    elif PlayerOne == "3" and PlayerTwo == "1":
        print(NameTwo + " beat " + NameOne + " with Rock")
        input()

    if PlayerOne == "2" and PlayerTwo == "3":
        print(NameTwo + " beat " + NameOne + " with Scissors")
        input()
    elif PlayerOne == "3" and PlayerTwo == "2":
        print(NameOne + " beat " + NameTwo + " with Scissors")
        input()

    if PlayerOne == PlayerTwo:
        print(NameOne + " and " + NameTwo + " tied.")
        input()

    #Rock Paper Scissors Grouping Player 2 and 3

    if PlayerTwo == "1" and PlayerThree == "2":
        print(NameThree + " beat " + NameTwo + " with Paper")
        input()
    elif PlayerTwo == "2" and PlayerThree == "1":
        print(NameTwo + " beat " + NameThree + " with Paper")
        input()

    if PlayerTwo == "1" and PlayerThree == "3":
        print(NameTwo + " beat " + NameThree + " with Rock")
        input()
    elif PlayerTwo == "3" and PlayerThree == "1":
        print(NameThree + " beat " + NameTwo + " with Rock")
        input()

    if PlayerTwo == "2" and PlayerThree == "3":
        print(NameThree + " beat " + NameTwo + " with Scissors")
        input()
    elif PlayerTwo == "3" and PlayerThree == "2":
        print(NameTwo + " beat " + NameThree + " with Scissors")
        input()

    if PlayerTwo == PlayerThree:
        print(NameTwo + " and " + NameThree + " tied.")
        input()    


    #Rock Paper Scissors Grouping Player 3 and 1

    if PlayerThree == "1" and PlayerOne == "2":
        print(NameOne + " beat " + NameThree + " with Paper")
        input()
    elif PlayerThree == "2" and PlayerOne == "1":
        print(NameThree + " beat " + NameOne + " with Paper")
        input()

    if PlayerThree == "1" and PlayerOne == "3":
        print(NameThree + " beat " + NameOne + " with Rock")
        input()
    elif PlayerThree == "3" and PlayerOne == "1":
        print(NameOne + " beat " + NameThree + " with Rock")
        input()

    if PlayerThree == "2" and PlayerOne == "3":
        print(NameOne + " beat " + NameThree + " with Scissors")
        input()
    elif PlayerThree == "3" and PlayerOne == "2":
        print(NameThree + " beat " + NameOne + " with Scissors")
        input()

    if PlayerThree == PlayerOne:
        print(NameThree + " and " + NameOne + " tied.")
        input()
    


    choice = input("1. Quit\n2. Continue\n")
    if choice == "1":
        break
