# Jothan Kelepolo
# 013
# 9/10/20

value = None
def factorial(num):
    out = 1
    for i in range(1,num+1):
        out = i * out
    return out

while value == None:
    try:
        value = int(input("Enter a number\n"))
    except:
        print("Please enter a valid integer\n")
print("The factorial of "+str(value)+" is "+str(factorial(value)))
