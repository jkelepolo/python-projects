# Jothan Kelepolo
# 012
# 9/9/20

value = None

def collatz(number):
    if number % 2 == 0:
        result = number // 2
        return result
    else:
        result = 3 * number + 1
        return result

while value == None:
    try:
        value = int(input("Input value\n"))
    except:
        print("Please enter a valid integer\n------")


value = collatz(value)
print(value)

while value != 1:
    value = collatz(value)
    print(value)
