#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the polynomialDivision function below.
def polynomialDivision(a, b, queries):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nabq = input().split()

    n = int(nabq[0])

    a = int(nabq[1])

    b = int(nabq[2])

    q = int(nabq[3])

    c = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = polynomialDivision(a, b, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
