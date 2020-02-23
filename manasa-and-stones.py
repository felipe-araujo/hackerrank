#!/bin/python3

import math
import os
import random
import re
import sys

def test_case14():
    with open('manasa-and-stones-input04.txt') as f:
        lines = f.readlines()
        T = int(lines[0])
        i = 1
        data = []
        for T_itr in range(T):
            n = int(lines[i])
            a = int(lines[i+1])
            b = int(lines[i+2])
            data.append((n,a,b))
            i+=3
    return data


# Complete the stones function below.
def stones(n, a, b):
    stones = [0]
    for i in range(1, n):
        stones = [x+a for x in stones] + [x+b for x in stones]
        stones = list(set(stones))
    stones = list(set(stones))
    stones.sort()
    return stones

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #T = int(input())
    data = test_case14()

    for n, a, b in data:
        #n = int(input())
        #a = int(input())
        #b = int(input())

        result = stones(n, a, b)

        print(' '.join(map(str, result)))
        

    
