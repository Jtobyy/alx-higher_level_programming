#!/usr/bin/python3
from functools import reduce

''' Order Number   Book Title and Author   Quantity    Price per Item '''
routine = [[34587, 'Learning Python', 'Mark Lutz', 4, 40.95],
           [98762, 'Programming Python', 'Mark Lutz', 5, 56.80],
           [77226, 'Head First Python', 'Paul Barry', 3, 32.95],
           [88112, 'Einführung in Python3', 'Bernd Klein', 3, 24.99]]

print ("initial list:", end = "\n")
for vals in routine:
    print ("{}".format(vals))
    
n_list = []
# multiplies product with item
for i in routine:
    red = reduce(lambda x, y: x * y, i[3:5])
    del i[3:5]
    if red < 100.0:
        red += 10
    i.append(red)

print("\nfirst reduced list:")
for vals in routine:
    print ("{}".format(vals))

n_list = []
for i in routine:
    j = list(filter(lambda x: isinstance(x, float) or isinstance(x, int), i))
    n_list.append(j)
print()
print("then: \n{}".format(n_list))

f_list = [(x, y) for x, y in n_list]
print("\nfinal list of tuples: \n{}".format(f_list))

