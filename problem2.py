# problem 2

# string="aaaaaaabbbbcccdddd"
string = input("Enter the String: ")
sett = set(string)
count = 0
char = ' '

for i in sett:
    if count < string.count(i):
        count = string.count(i)
        char = i
print(char)
