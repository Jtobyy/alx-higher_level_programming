#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except (IndexError, ZeroDivisionError, TypeError, ValueError) as inst:
        print("Exception: {}".format(inst), file=sys.stderr)
        return None
