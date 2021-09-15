#!/usr/bin/python3

import hidden_4

names = dir(hidden_4)
for mods in names:
    if mods[0] != '_' and mods[1] != '_':
        print("{}".format(mods))
if __name__ == "__main__":
    pass
