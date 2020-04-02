#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
# [0 1 2 3], m=2 range(0, 2)

def birthday(s, d, m):
    count = 0
    for k in range(0, len(s)-m+1):        
        if sum(s[k:k+m]) == d:
            count +=1
    return count


if __name__ == '__main__':
    
    #n = int(input().strip())

    s = [1, 2, 1, 3, 2]

    dm = [3, 2]

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)
