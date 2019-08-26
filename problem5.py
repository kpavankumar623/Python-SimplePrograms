#problem 5

restaurants = [ [ "Acme", "Italian", 2, 4, 3, 5],[ "Flintstone", "Steak", 5, 2, 4, 3, 3, 4],
               [ "BellaTroy", "Italian", 1, 4, 5] ]

for i in restaurants:
    if(i[1] == "Italian"):
        if 1 not in i[2:] and 5 in i[2:]:
            print(i[0] ,end=",")