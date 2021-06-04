
dice_1 = int(input("Sides on dice one\n"))
dice_2 = int(input("Sides on dice two\n"))
target = int(input("Target number\n"))
count = 0
table = []

for i in range(1, dice_1+1):
    for j in range(1, dice_2+1):
        
        if (i+j) == target:
            count += 1
            
        table.append(str(i) + "+" + str(j) + "=" + str(i+j))
        

print("Possibilities: " + str(count))
print(table)
input()