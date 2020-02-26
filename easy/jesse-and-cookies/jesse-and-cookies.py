#!/bin/python3

import os
import sys
from collections import deque
from math import log, pow
import bisect
#
# Complete the cookies function below.
#
def noprint(*args):
    pass
debug = print
def cookies(k, A):
    #
    # Write your code here.
    #
    #A.sort()
    smaller = list(filter(lambda x: x<k, A))
    debug('len(smaller)', len(smaller))
    bigger = list(filter(lambda x: x>=k, A))
    debug('len(bigger)', len(bigger))

    smaller.sort()
    bigger.sort()
    count = 0
    while smaller:
        #smaller.sort()
        #bigger.sort()
        repetitions = check_repetitions(smaller)    
        count += 1

        combined = smaller.pop(0)
        if smaller:
            mix = smaller.pop(0)
        elif bigger:
            mix = bigger.pop(0)            
        else:
            debug('len(smaller)', len(smaller))
            debug('len(bigger)', len(bigger))
            debug('count=', count)
            return -1
                
        combined += 2*mix

        if combined <k:            
            bisect.insort(smaller, combined)
            #smaller.append(combined)
            if repetitions > 1:
                count += repetitions - 1
                debug('repetitions=', repetitions, '@smaller')
                smaller = smaller[2*repetitions-2:]
                smaller.extend([combined] * (repetitions -1))
                smaller.sort()
        else:
            debug('len(bigger)', len(bigger))            
            bisect.insort(bigger, combined)
            #bigger.append(bigger)
            if repetitions > 1:
                count += repetitions - 1
                debug('repetitions=', repetitions, '@bigger')
                smaller = smaller[2*repetitions-2:]
                bigger.extend([combined] * (repetitions -1))
                bigger.sort()            

        #if repetitions > 1:
        #    smaller
    
    debug(smaller)
    
    debug(list(filter(lambda x: x<k, bigger)))
    return count

def check_repetitions(array):
    count = 0
    for i in range(0, len(array)-1, 2):
        if array[i] == array[i+1]:
            count +=1
        else:
            break
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
