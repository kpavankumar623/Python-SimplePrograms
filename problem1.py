#problem1


notes = [10, 20, 50, 100, 500, 2000]
amount = int(input("Enter the some Amount:"))
result = {}
if (amount % 2000 != amount):
    result[2000] = amount // 2000
    amount = amount % 2000
if (amount % 500 != amount):
    result[500] = amount // 500
    amount = amount % 500
if (amount % 100 != amount):
    result[100] = amount // 100
    amount = amount % 100
if (amount % 50 != amount):
    result[50] = amount // 50
    amount = amount % 50
if (amount % 20 != amount):
    result[20] = amount // 20
    amount = amount % 20
if (amount % 10 != amount):
    result[10] = amount // 10

for k, v in result.items():
    print(str(k) + "=" + str(v), end=",")
