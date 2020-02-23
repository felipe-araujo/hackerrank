#!/bin/python3

import math
import os
import random
import re
import sys
from timeit import default_timer as timer

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    s = list(s)
    offset, s = reducePalindrome(s)

    if checkPalindrome(s):
        return -1
    for i in range(len(s)):
        #trimmed = s[:i]+s[i+1:]
        if checkPalindromeWithIndex(s, i):
            return i+offset
    return -1

def checkPalindrome(s):
    size = len(s)
    for i in range(int(size/2)):
        if s[i] != s[size-i-1]:
            return False
    return True

def reducePalindrome(s):
    size = len(s)
    for i in range(int(size/2)):
        if s[i] == s[size-i-1]:
            continue
        else:
            break
    return i, s[i:size-i]
#4
#abdbca



def checkPalindromeWithIndex(s, idx):
    size = len(s)
    sep = int(size/2)

    outer = min(idx, size-idx-1)
    for i in range(outer):
        if s[i] != s[size-i-1]:
            return False
    dleft = 0
    dright = 0
    if idx < sep:
        dleft = 1
    else:
        dright = 1

    for i in range(outer, sep):
        if s[i+dleft] != s[size-i-1-dright]:
            return False
    return True

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        s = input()

        start = timer()
        result = palindromeIndex(s)
        end = timer()        
        fptr.write(str(result) + '\n')
        print('elapsed: ', end - start, '\n')

    fptr.close()
