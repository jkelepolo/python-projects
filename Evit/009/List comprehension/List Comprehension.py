# Jothan Kelepolo
# 009
# 8/26/2020

import os
import sys
import random

while True:
    listSize = int(input("How large do you want the list to be?\n"))

    maxNumberRange = int(input("What do you want the max number to be in each list slot?\n"))

    numberList = []

    evenNumbers = []


    for i in range(0,listSize):
        numberList.append(random.randint(1,maxNumberRange))


    for number in numberList:
        if number % 2 == 0 and number not in evenNumbers:
            evenNumbers.append(number)


    # Sort even numbers
    evenNumbers.sort()

    print("Current List\n"+str(numberList))
    print("\nEven numbers in the list\n"+str(evenNumbers))

    q = input("\nPress enter to continue\n(or 'q' to quit)")
    if q == "q":
        break
    else:
        os.system('cls')
