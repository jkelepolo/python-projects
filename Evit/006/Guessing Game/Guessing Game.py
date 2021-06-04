# Jothan Kelepolo
# Project 006
# 8/19/2020

import random
import sys
import os


while True:
    os.system('cls')
    tries = 1
    playing = "true"
    numberlist = int(input("How many numbers do you want to guess from?\n"))
    number = random.randint(1,numberlist)

    
    print("The Computer has chosen a number between 1 and "+str(numberlist)+"\n")


    
    while playing == "true":
        guess = int(input("Guess a whole number 1-"+str(numberlist)+"\n")) 
        if guess == number:
            print("You guessed right! The number was, "+str(number))
            print("It only took you "+str(tries)+" tries!")
            playing = "false"
            input()
        elif guess > number:
            print("\nYour guess is too high! Guess again.\n")
            tries = tries + 1
        elif guess < number:
            print("\nYour guess is too low! Guess again.\n")
            tries = tries + 1
        elif guess == "quit" or guess == "q":
            break
            


    continuegame = input("Continue? \ny/n: ")
    if continuegame == "n":
        break
        
