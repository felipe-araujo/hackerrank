#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    pages = {}
    p = 1
    for i in range(0, len(arr)):
        problems = 0
        while problems < arr[i]:
            start = problems+1
            end = start + min(k, arr[i]-problems)
            pages[p] = [x for x in range(start, end)]
            problems += k
            p +=1
    magic = []
    print(pages)
    for page in pages:
        if page in pages[page]:
            magic.append(page)
    return len(magic)

            


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #nk = input().split()

    #n = int(nk[0])
    n = 10

    #k = int(nk[1])
    k = 5

    arr = list(map(int, '3 8 15 11 14 1 9 2 24 31'.rstrip().split()))

    result = workbook(n, k, arr)

    print(result)