#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        quo = a / b
    except ZeroDivisionError:
        quo = None
    finally:
        str = f'Inside result: {quo}'
        print("{}".format(str))
    return quo
