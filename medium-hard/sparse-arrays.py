#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    strings = list(map(str.strip, strings))
    queries = list(map(str.strip, queries))
    counter = {}
    for s in strings:
        if s not in counter:
            counter[s] = 1
        else:
            counter[s] +=1
    #print(counter)
    result = [0] * len(queries)
    for i, q in enumerate(queries):
        if q in counter:
            result[i] = counter[q]
    return result

if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
