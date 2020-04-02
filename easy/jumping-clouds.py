#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    i = 0
    # 0 0 0
    # 0 0 1
    # 0 1 0

    if len(c) < 3:
        return 1

    while i < len(c)-3:
        print('i: ', i)
        if c[i] == 0 and c[i+1] == 0 and c[i+2] == 0:
            i = i + 2
            count += 1
        if c[i] == 0 and c[i+1] == 0 and c[i+2] == 1:
            i = i + 1
            count +=1
        if c[i] == 0 and c[i+1] == 1 and c[i+2] == 0:
            i = i + 2
            count +=1

    print('i no final do loop:', i)
    print('len(c) = ', len(c))
    
    # 0 1
    # 0 0
    if i < len(c)-1:
        count +=1
            
    return count
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())
    s = '0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 0 0 0 1 0 0 1 0 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1 0 1 0 1 0 0 0 0 0 0 1 0 0 0'

    c = list(map(int, s.rstrip().split()))

    #c = [0, 0]

    result = jumpingOnClouds(c)

    print(result)