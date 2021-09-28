#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    c = 0
    len_ = 0
    while (c < x):
        try:
            print("{:d}".format(my_list[c]), end="")
            len_ += 1
        except (ValueError, TypeError):
            continue
        finally:
            c += 1
    print()
    return len_
