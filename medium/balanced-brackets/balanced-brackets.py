#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    match = {')': '(', ']': '[','}': '{'}

    for c in s:
        if c in opening:
            stack.append(c)
        elif c in closing:
            if not stack:
                return 'NO'
            el = stack.pop()
            if el != match[c]:
                return 'NO'
        else:
            return 'NO!!!'
        
    if not stack:
        return 'YES'
    else:        
        return 'NO'

if __name__ == '__main__':
    
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
