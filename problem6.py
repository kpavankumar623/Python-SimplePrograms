# problem 6

dict = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'), '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'), '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'), '9': ('w', 'x', 'y', 'z')}

number = "9999335533"
temp = number[0]
count = 0
list = []
for i in range(len(number)):
    if temp == number[i]:
        count += 1
    else:
        list.append(dict[temp][count - 1])
        temp = number[i]
        count = 1
    if i == (len(number) - 1):
        list.append(dict[temp][count - 1])

for i in list:
    print(i, end="")