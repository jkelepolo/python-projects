# Jothan Kelepolo
# Project 007
# 8/20/20

import sys
import os
import random

# Alterable Variables
minimumListCount = 5
maximumListCount = 20

minimumNumberRange = 0
maximumNumberRange = 100


# Main Loop
while True:

    # Reset lists
    a = []
    b = []
    c = []

    # Generate lists
    for i in range(0, random.randint(minimumListCount, maximumListCount)):
      a.insert(i, random.randint(minimumNumberRange, maximumNumberRange))

    for i in range(0, random.randint(minimumListCount, maximumListCount)):
      b.insert(i, random.randint(minimumNumberRange, maximumNumberRange))

    # Test for list overlap
    for i in range(0, len(a)):
        if a[i] in b:
            if a[i] not in c:
                c.insert(i, a[i])

                

    print("Shared items: "+str(c))


    print("List a: "+str(a))
    print("List b: "+str(b))

    
    q = input("\nPress Enter\n(Or type 'q' to exit)\n")
    if q == "q":
        break
    os.system('cls')
