import random
Heads = 0
Tails = 0
LIST = []

flips = int(input("How many times do you want to flip the coin?\n"))

for flip in range(flips):
    rand = random.randint(0,1)
    if rand == 0:
        Heads += 1
        LIST.append("H")
    elif rand == 1:
        Tails += 1
        LIST.append("T")

print("Heads: "+str(Heads))
print("Tails: "+str(Tails))
print(LIST)
input()