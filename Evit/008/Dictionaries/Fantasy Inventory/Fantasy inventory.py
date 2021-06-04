# Jothan Kelepolo
# 008.2
# 8/25/2020

import sys
import os
import random

acquiredItems = ""
# Create inventory
inventory = {'rope':0, 'sword':0, 'shield':0, 'dragon scales':0, 'gold coin':0,"dagger":0,
             'ruby':0}

# loot tables
dragonLoot = {'gold coin': 10, 'dagger':1, 'ruby':1, 'dragon scales':30}

# display inventory
def displayInventory():
    itemCount = list(inventory.values())
    count = 0
    totalItems = 0
    print("\nInventory\n---------")
    for i in inventory:
        if itemCount[count] != 0:
            print(i + ": " + str(itemCount[count]))
            print("---------\n")
        totalItems += itemCount[count]
        count += 1
    print("Total number of items: " + str(totalItems))

# add item to inventory
def addToInventory(addedItems):
    global inventory
    global acquiredItems
    acquiredItems = ""
    maxDrop = list(dragonLoot.values())
    count = 0

    for i in addedItems:
        if i in inventory:
            maxItemDrop = random.randint(0,maxDrop[count])
            inventory[i] += maxItemDrop
            acquiredItems = acquiredItems + "\n+"+str(maxItemDrop)+" "+ str(i)
            count += 1
# main loop
while True:
    
    choice = input("\n1. Attack Dragon\n2. View inventory\n3. Quit\n")

    if choice == "1":
        os.system('cls')
        print("You attacked and killed a Dragon")
        addToInventory(dragonLoot)
        print(acquiredItems)
        displayInventory()
        
    elif choice == "2":
        os.system('cls')
        displayInventory()
    elif choice == "3":
        break

    else:
        os.system('cls')


    
