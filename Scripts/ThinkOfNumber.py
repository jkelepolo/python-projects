import random
import os

answer = None
tries = 1
maxGuess = int(input("Pick a large number\n"))
maxGuess += 1
minGuess = maxGuess + 1
while minGuess > maxGuess:
    os.system('cls')
    minGuess = int(input("Pick a small number\n(Lower than your large number)\n"))

estimated_tries = 0
if abs(maxGuess) > abs(minGuess):
    temp = maxGuess
else:
    temp = abs(minGuess)
    
while temp > 0:
    estimated_tries += 1
    temp = round(temp/2)

print("\nGreat!\nI bet I can guess your number in under " + str(estimated_tries) + " tries!")
input("Think of a number between "+str(minGuess)+" and "+str(maxGuess-1)+"\n(Enter to continue)")
os.system('cls')

while answer != "1":

    guess = minGuess + round((maxGuess-minGuess)/2)
    
    answer = input("Is your number " + str(guess) +"?\n1.yes\n2.higher\n3.lower\n")
    
    
    os.system('cls')
    
    if answer == "2":
        minGuess = guess
        
            
        tries += 1
    elif answer == "3":
        maxGuess = guess
        
        
        tries += 1
    elif answer == "1":
        input("That was easy! It only took me " + str(tries) + " tries!")


