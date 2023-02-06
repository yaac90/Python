#!/usr/bin/python3
multiple_variables, name, age, adress = [ 20, 40, 10, 99 ], 'yuber', 33, 'aven. lincoln 1234' 
south_America = { 'pais1': 'Colombia', 'pais2':'Venezuela', 'pais3':'Ecuador', 'pais4':'Brasil' }

# Printing the list of the dictionary.
print(list(enumerate(south_America)))

# Printing the length of the dictionary.
print(len(south_America))

# Printing a list of numbers from 0 to 9.
print(tuple(range(10)))

# Printing the methods of the range object.
print(dir(range))

# It's printing the sum of the values of the list.
print(sum(multiple_variables))
