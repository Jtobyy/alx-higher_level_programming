#!/usr/bin/python3
'''
Inherits from list and does some other things
'''


class MyList(list):
    '''
    Inherits from list
    '''
    def print_sorted(self):
        print(sorted(self))
