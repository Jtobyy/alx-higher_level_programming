#!/usr/bin/python3
import random

arr_ = []
for i in range(10):
     arr_.append(random.randint(1, 50))
print("initial array: {}".format(arr_))

def bubblesort(arr):
     lim = len(arr) - 1
     j = lim
     while j >= 0:
          i = 0
          while i < lim:
               if arr[i] > arr[i + 1]:
                    tmp = arr[i + 1]
                    arr[i + 1] = arr[i]
                    arr[i] = tmp
               i += 1
          j -= 1
     return arr

bubblesort(arr_)
print("bubble sorted array: {}".format(arr_))
