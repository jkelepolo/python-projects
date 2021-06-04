# Jothan Kelepolo
# Project RPS
# 8/18/2020
import sys

NameOne = input("Player 1:\n")
NameTwo = input("Player 2:\n")
while True:
# ask for Rock Paper or Scissors
    print("\nRock > Scissors, Paper > Rock, Scissors > Paper")
    print("Player 1:")
    PlayerOne = input("1. Rock \n2. Paper \n3. Scissors\n")
    print("\n"*100)

    print("Player 2:")
    PlayerTwo = input("1. Rock \n2. Paper \n3. Scissors\n")


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
        print("Player 2 beat Player 1 with Rock")
        print(NameTwo + " beat " + NameOne + " with Rock")
        input()

    if PlayerOne == "2" and PlayerTwo == "3":
        print(NameTwo + " beat " + NameOne + " with Scissors")
        input()
    elif PlayerOne == "3" and PlayerTwo == "2":
        print(NameOne + " beat " + NameTwo + " with Scissors")
        input()

    if PlayerOne == PlayerTwo:
        print("It was a tie.")
        input()

    choice = input("1. Quit\n2. Continue\n")
    if choice == "1":
        break
