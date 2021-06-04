string_array = input("Input any string of characters\n\n")
sorting = True
string_values = ""

while sorting:
    sorting = False
    for c in range(0,len(string_array)):
        try:
            if ord(string_array[c+1].lower()) < ord(string_array[c].lower()):
                sorting = True
                
                str_list = list(string_array)
                
                temp = string_array[c]
                str_list[c] = str_list[c+1]
                str_list[c+1] = temp
                string_array = ''.join(str_list)
        except:
            pass

print("\nSorted characters\n"+string_array)

for c in str_list:
    string_values += str(ord(c))+","
    
print(string_values)