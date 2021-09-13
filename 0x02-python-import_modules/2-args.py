#!/usr/bin/python3

import sys

length = len(sys.argv) - 1
argv = sys.argv[1:]

if length == 0:
    print("{} arguments.".format(length))
elif length == 1:
    print("{} argument:\n{}: {}".format(length, 1, sys.argv[1]))
else:
    c = 1
    print("{} arguments:".format(length))
    for args in argv:
        print("{}: {}".format(c, args))
        c += 1
if __name__ == "__main__":
    pass
