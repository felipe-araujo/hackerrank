#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    #count = 0
    i = 0
    while len(s) > i and len(t) > i and s[i] == t[i]:
        i +=1
    print(i)
    to_remove = len(s) - i
    to_insert = len(t) - i
    if (to_remove + to_insert) == k:
        print('to_remove + to_insert:' , to_remove + to_insert)
        return 'Yes'
    elif (to_remove + to_insert) > k:
        print('2to_remove + to_insert:' , to_remove + to_insert)
        return 'No'    
    elif (len(s) + len(t)) <= k and (len(s) + len(t)) % 2 ==0:
        print('3to_remove + to_insert:' , to_remove + to_insert)
        return 'Yes'
    else:
        return 'No'

def test_case_01():
    return 'abcd', 'abcdert', 10, 'No'
def test_case_02():
    return 'y', 'yu', 2, 'No'

def test_case_03():
    return 'asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv',\
    'asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv',\
    20,\
    'Yes'





if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = 'ashley'

    t = 'ash'
    k = 2
    e = 'No'

    #s,t, k,e  = test_case_01()
    #s,t, k,e  = test_case_02()
    s,t, k,e  = test_case_03()

    result = appendAndDelete(s, t, k)

    print(result, e)
