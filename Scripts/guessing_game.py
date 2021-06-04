import random
import os

guess = None

maxNumber = int(input("How many number to guess from?\n( 0 - ???)\n"))


while True:
    tries = 0
    target = random.randint(0, maxNumber)
    while not guess == target:
        guess = int(input("Guess between 0 - " + str(maxNumber) + "\n"))
     
        if guess > target:
            print("\nLower!")
        elif guess < target:
            print("\nHigher!")
        elif guess == target:
            print("Congrats! You got it! The answer was: "+ str(target) + "\n Tries: " + str(tries+1))
        
        tries += 1
    q = input("Press enter to play again\n'q' to quit\n")
    
    if q == 'q':
        os.system('clear')
        break
    else:
        os.system('clear')
        q = ''