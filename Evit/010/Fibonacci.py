# Jothan Kelepolo
# 010
# 9/1/2020

import os

def fibonacci():
    count = int(input("How many numbers do you want to generate in the sequence?\n"))
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib

while True:

    print(fibonacci())
    q = input("\nEnter to continue\n(Or 'q' to exit)")
    if q == "q":
        break
    else:
        os.system("cls")
