# Jothan Kelepolo
# 011.1
# 9/8/20

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

word = input("Enter word to be reversed: ")

print(reverse(word))
