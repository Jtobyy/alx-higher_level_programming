#!/usr/bin/python3
"""
Finds a peak in the list of unsorted integers
"""

def find_peak(list_of_integers):
    """
    Finds and returns a peak in the list of an unsorted integer
    """
    if len(list_of_integers) == 0:
        return None
    else:
        i = 1
        peak = list_of_integers[0]
        try:
            while i < len(list_of_integers):
                if(peak < list_of_integers[i]):
                    peak = list_of_integers[i]
                i += 1
        except IndexError:
            pass
        return peak
