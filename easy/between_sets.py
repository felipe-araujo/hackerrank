#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    counter = 0
    b.sort()
    for n in range(1, 101):
        valid = True
        for ai in a:
            if n % ai != 0:
                valid = False
                break
        for bi in b:
            if bi % n != 0:
                valid = False
                break
        if valid:
            counter += 1
    return counter
        


if __name__ == '__main__':
    arr = [1]
    brr = [100]

    total = getTotalX(arr, brr)

    print(total)
