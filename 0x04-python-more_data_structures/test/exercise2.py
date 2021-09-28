#!/usr/bin/python3
from functools import reduce

''' Write a program which returns a list of two tuples with (order number, total amount of order). '''

orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
           [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
           [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

# b_list = reduce(lambda x: x if (x[0],  ,a_list)
a_list = reduce(lambda x, y: x + y, orders)
b_list = list(map(lambda x: x if isinstance(x, int) else x[1] * x[2], a_list))
c_list = []
d_list = []
c = reduce(lambda x, y: x if isinstance(x, int) or isinstance(y, int) else x + y, b_list)
del b_list[:1]
d = reduce(lambda n, m: n if isinstance(n, int) or isinstance(m, int) else n + m, b_list)
c_list.append(c)
d_list.append(d)
#b_list = list(map(lambda x: x[1] * x[2], reduce(lambda x, y: x + y, a_list)))

print("{}\n".format(a_list))
print("{}".format(b_list))
print("{}".format(c_list))
print("{}".format(d_list))
