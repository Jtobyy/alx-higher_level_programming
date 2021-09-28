#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []
    while (i < list_length):
        try:
            quo = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            quo = 0
        except TypeError:
            print("wrong type")
            quo = 0
        except IndexError:
            print("out of range")
            quo = 0
        finally:
            new_list.append(quo)
            i += 1
    return new_list
