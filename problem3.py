#problem 3

numbers = [1,2,3,4,5]
even_count = 0
odd_count = 0
for i in numbers:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

remove_count = 0
if(odd_count < even_count):
    for i in numbers:
        if i % 2 != 0:
            numbers.remove(i)
    remove_count = odd_count
else:
    for i in numbers:
        if i % 2 == 0:
            numbers.remove(i)
    remove_count = even_count

print(numbers)
print("Removed elemts:{} ".format(remove_count))
