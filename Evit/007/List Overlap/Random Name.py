# Jothan Kelepolo
# Project 007.1
# 8/20/20

import os
import sys
import random

a = ["Dawson", "Kannon", "Amari", "Zander", "Francisco", "Jake", "Konrad", "Simon", "Jothan", "Kenan", "Jackson", "Kaleb", "Drew", "Ethan", "Connor", "Adrian", "Moroni", "Alec", "Michael", "Gabriel", "Cole", "Andrew", "Brady"]
b = a

while True:
    input("Press Enter to generate new name\n")
    os.system('cls')
    choice = random.randint(0,len(b)-1)
    print("Random name: " + b[choice])
    b.remove(b[choice])
    if len(b) <= 0:
        a = ["Dawson", "Kannon", "Amari", "Zander", "Francisco", "Jake", "Konrad", "Simon", "Jothan", "Kenan", "Jackson", "Kaleb", "Drew", "Ethan", "Connor", "Adrian", "Moroni", "Alec", "Michael", "Gabriel", "Cole", "Andrew", "Brady"]
        b = a


