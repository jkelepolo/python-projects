# Jothan Kelepolo
# 011.1
# 9/8/20

choice = input("Convert\n1. Celsius to Fahrenheit\n2.Fahrenheit to Celsius\n")
degree = int(input("\nEnter temperature\n"))

if choice == "1":
    result = int(round((9 * degree) / 5 + 32))
    print(str(degree) + "C in Fahrenheit is " + str(result))
elif choice == "2":
    result = int(round((degree - 32) * 5 / 9))
    print(str(degree) + "F in Celsius is " + str(result))


