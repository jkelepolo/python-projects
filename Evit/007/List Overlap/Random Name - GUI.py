# Jothan Kelepolo
# Project 007.1
# 8/20/20
from tkinter import *
import random
import time


root = Tk()
root.configure(bg="black")
root.title("Random Name")


a = ["Dawson", "Kannon", "Amari", "Zander", "Francisco", "Jake", "Konrad", "Simon", "Jothan", "Kenan", "Jackson", "Kaleb", "Drew", "Ethan", "Connor", "Adrian", "Moroni", "Alec", "Michael", "Gabriel", "Cole", "Andrew", "Brady"]
b = a

#Functions
def newName():
    global a
    global b

    if len(b) <= 0:
        a = ["Dawson", "Kannon", "Amari", "Zander", "Francisco", "Jake", "Konrad", "Simon", "Jothan", "Kenan", "Jackson", "Kaleb", "Drew", "Ethan", "Connor", "Adrian", "Moroni", "Alec", "Michael", "Gabriel", "Cole", "Andrew", "Brady"]
        b = a
        choice = random.randint(0,len(b)-1)
        nameLabel.config(text=b[choice])
        b.remove(b[choice])
        print(str(len(b)))
        
    else:     
        choice = random.randint(0,len(b)-1)
        nameLabel.config(text=b[choice])
        b.remove(b[choice])
        print(str(len(b)))
        
    

#Define Labels
sizeLabel = Label(root, text = " ", padx=300, pady=100, bg = "black")
nameLabel = Label(root, text = "Name",pady=100, bg = "black", fg = "white",font=("Courier", 44))

#Define buttons
nameButton = Button(root, text = "New Name", bg = "black", fg = "white", padx = 20, command = newName, font=("Courier", 44))

#Pack Labels
nameLabel.pack()

#Pack Buttons
nameButton.pack()

#Pack Sizing label
sizeLabel.pack()

root.mainloop()
