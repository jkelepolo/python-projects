# Jothan Kelepolo
# 011.1
# 9/8/20

numbers = [1,2,3,4,5,6,7,8,9]
even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even = even + 1
    elif number % 2 != 0:
        odd = odd + 1
print(numbers)
print("Even: "+str(even))
print("Odds: "+str(odd))
