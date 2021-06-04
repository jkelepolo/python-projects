import random
import os

tries = 1

maxGuess = 1000000
minGuess = 0
guess = 0


target = int(input("Input a number between " + str(minGuess) + " and " + str(maxGuess)+"\n"))
os.system('cls')

while guess != target:
    guess = minGuess + round((maxGuess-minGuess)/2)
    
    if guess > target:
        maxGuess = guess
        print(str(guess)+" is > target")
    elif guess < target:
        minGuess = guess
        print(str(guess)+" is < target")
    else:
        print("The answer is " + str(guess) + "\n It only took " + str(tries) + " tries!")
    
    tries += 1

input()
