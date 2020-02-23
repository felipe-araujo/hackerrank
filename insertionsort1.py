#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    pivot = arr[-1]        
    for i in range(n-2, -1, -1):
        #print('i: ', i, ', pivot:', pivot, ', arr:', arr)
        if arr[i] < pivot:
            arr[i+1] = pivot
            print(' '.join(map(str, arr)))
            #print('will break')
            pivot = None
            break
        else:
            arr[i+1] = arr[i]
            print(' '.join(map(str, arr)))
            #arr[i-1] = pivot
    if pivot:
        arr[0] = pivot
        print(' '.join(map(str, arr)))    
        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
