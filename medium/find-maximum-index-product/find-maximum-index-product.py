#!/bin/python3

import os
import sys

def noprint(*args):
    pass

debug = print

# Complete the solve function below.
def solve(arr):
    return naive_solution(arr)


def naive_solution(arr):    
    max_product = 0
    
    prev_left_i = 0
    prev_right_i = 0
    prev_left = 0
    prev_right = 0
    prev_element = None
    max_all = max(arr)
    max_indexes = [index for index, value in enumerate(arr) if value==max_all]
    max_index = max(max_indexes)+1 # 1-based indexes
    max_so_far = arr[0]
    min_so_far = arr[0]

    size = len(arr)
    debug('len(arr)=', size)

    # TODO check if found index is too low to 
    # eventually give a bigger product than the current one.
    for i, element in enumerate(arr):
        left, right = 0, 0
        offset_left, offset_right = 0, 0

        if element > max_so_far:
            max_so_far = element
            debug('bigger than max_so_far')
            prev_left_i = None
            prev_right = None 
            continue
        if element < min_so_far:
            min_so_far = element
        

        if prev_element and prev_element == element:
            debug('early return, i=', i)
            continue
        if prev_element and prev_element < element:
            offset_left = prev_left_i if prev_left_i else 0#+1
            offset_right = prev_right_i-1 if prev_left_i else 0
        
        #if prev_element and prev_element > element \
        #        and i*(prev_right_i) < max_product:
        #        debug('early return, i*(prev_right)=', (i-1)*(prev_right_i))
        #        prev_left_i = 0
        
        for k, target in enumerate(reversed(arr[:i+offset_left])):
            if target > element:
                prev_left_i = k
                left = (i+1)-(k+1) + offset_left
                break
        if left == 0:
            prev_left_i = None
            debug('early return, left=', left)
            continue
        if left * (size+1) < max_product:
            prev_left_i = None
            debug('early return, left * size=', left * max_index, 'max_product=', max_product)
            continue

        for k, target in enumerate(arr[i+1+offset_right:]):
            if target > element:
                prev_right_i = k
                right = (i+1)+(k+1) + offset_right
                break
        product = left * right
        prev_element = element
        prev_left = left
        prev_right = right        
        #print('[index=', i, ' ] left=', left, ', right=', right, 'product=', product)
        #print('offset left=', offset_left, ', offset right=', offset_right)
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
