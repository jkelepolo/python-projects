# Jothan Kelepolo
# 009.1
# 8/26/2020

import sys
import os
import random

while True:

    flipCount = int(input("How many times do you want to flip the coin?\n"))

    heads = 0

    tails = 1

    coin = heads

    headFlips = {"flips": 0, "current streak": 0, "6 streak":0, "max streak":0}

    tailFlips = {"flips": 0, "current streak": 0, "6 streak":0, "max streak":0}

    for i in range(0,flipCount):
        coin = random.randint(heads,tails)
        if coin == heads:
            tailFlips["current streak"] = 0
            headFlips["flips"] = headFlips["flips"] + 1
            headFlips["current streak"] = headFlips["current streak"] + 1

            if headFlips["current streak"] > headFlips["max streak"]:
                headFlips["max streak"] = headFlips["current streak"]

            if headFlips["current streak"] % 6 == 0 and headFlips["current streak"] >= 6:
                headFlips["6 streak"] = headFlips["6 streak"] + 1
            
        elif coin == tails:
            headFlips["current streak"] = 0
            tailFlips["flips"] = tailFlips["flips"] + 1
            tailFlips["current streak"] = tailFlips["current streak"] + 1

            if tailFlips["current streak"] > tailFlips["max streak"]:
                tailFlips["max streak"] = tailFlips["current streak"]

            if tailFlips["current streak"] % 6 == 0 and tailFlips["current streak"] >= 6:
                tailFlips["6 streak"] = tailFlips["6 streak"] + 1


    print("\nHead flip data\n"+str(headFlips))
    print("\nTail flip data\n"+str(tailFlips))
    q = input("\nEnter to continue\n(Or enter 'q' to quit)\n")
    if q == "q":
        break
    else:
        os.system('cls')
          
# 20,000,000 flips
# 
# 1. 1 min 8s 80ms
#
# 2. 1 min 9s 42ms
# 
# 3. 1 min 8s 96ms
