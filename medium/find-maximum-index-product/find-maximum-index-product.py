#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(arr):
    return naive_solution(arr)


def naive_solution(arr):    
    max_product = 0
    for i, element in enumerate(arr):
        left, right = 0, 0
        for k, target in enumerate(reversed(arr[:i])):
            if target > element:
                left = (i+1)-(k+1)
                break

        for k, target in enumerate(arr[i+1:]):
            if target > element:
                right = (i+1)+(k+1)
                break
        product = left * right
        #print('[index=', i, ' ] left=', left, ', right=', right, 'product=', product)
        if product > max_product:
            max_product = product
    return (max_product)



if __name__ == '__main__':
    fptr = sys.stdout
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
