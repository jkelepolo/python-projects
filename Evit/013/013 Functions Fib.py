# Jothan Kelepolo
# 013
# 9/10/20

def fib(n):
    out = []
    for i in range(0,n):
        if len(out) > 2:
            out.append(out[i-2]+out[i-1])
        else:
            out.append(i)
        out[0] = 1
    return out
            
inNum = None

while inNum == None:
    try:
        inNum = int(input("Input Number\n"))
    except:
        print("Enter a valid integer")



print(fib(inNum))