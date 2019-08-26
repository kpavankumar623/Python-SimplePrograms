# problem 4

states = {'New Hampshire': ['Concord', 'Hanover'],'Massachusetts': ['Boston', 'Concord', 'Springfield'],
           'Illinois': ['Chicago', 'Springfield', 'Peoria'] }

cities = {}
for k,v in states.items():
    for i in v:
        if i in cities:
            cities[i] = [cities[i],k]
        else:
            cities[i] = k;
print("cities = {}".format(cities))