# Jothan Kelepolo
# 011.1
# 9/8/20

for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    elif i % 3 == 0:
        print("fizz")
        continue
    elif i % 5 == 0:
        print("buzz")
        continue
    print(i)
