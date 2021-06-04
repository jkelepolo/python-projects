# Jothan Kelepolo
# Project 008.1
# 8/24/2020

import sys
import os


# Main loop
while True:
    inputNumber = 0

    # Prevent iteration from getting dangerously large by capping it at 10,000,000
    while inputNumber > 10000000 or inputNumber == 0:
        if inputNumber > 10000000:
            print(str(inputNumber) + " is too large! Enter a number less than or equal to 10,000,000.")
        inputNumber = int(input("Input number to find primality: "))
     
        
    listRange = list(range(1,inputNumber+1))

    divisorList = []
    
    # Iterate through list and find the modulous
    for num in listRange:
        if inputNumber % num == 0:
            divisorList.append(num)

    print(divisorList)
    if len(divisorList) != 2 and inputNumber != 1:
        print(str(inputNumber)+" is NOT prime!")
    else:
        print(str(inputNumber)+" is Prime!")

    # Loop escape sequence
    q = input("\nEnter to continue\n(Or enter 'q' to quit)\n")
    os.system('cls')
    if q == "q":
        break
    else:
        q = " "
