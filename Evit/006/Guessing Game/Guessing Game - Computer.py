# Jothan Kelepolo
# Project 006.1
# 8/19/2020

import random
import sys
import os


while True:
    os.system('cls')
    tries = 1
    playing = "true"
    minimum = 1
    numberlist = int(input("How many numbers do you want the computer to guess from?\n"))
    maximum = numberlist

    os.system('cls')
    number = int(input("Choose a number between 1 and "+str(numberlist)+" for the computer to choose from\n"))
    
    
    print("You have chosen a number between 1 and "+str(numberlist)+"\n")


    
    while playing == "true":
        guess = random.randint(minimum,maximum) 
        if guess == number:
            print("The computer guessed right! The number was, "+str(number))
            print("It only took "+str(tries)+" tries!")
            playing = "false"
        elif guess > number:
            print("The Computer guesses "+str(guess))
            print("The guess is too high!\n")
            maximum = guess-1
            tries = tries + 1
        elif guess < number:
            print("The Computer guesses "+str(guess))
            print("The guess is too low!\n")
            minimum = guess+1
            tries = tries + 1
        elif guess == "quit" or guess == "q":
            break
       
            


    continuegame = input("Continue? \ny/n: ")
    if continuegame == "n":
        break
        
