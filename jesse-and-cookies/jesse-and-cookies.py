#!/bin/python3

import os
import sys
from collections import deque
from math import log, pow
#
# Complete the cookies function below.
#
def cookies(k, A):
    #
    # Write your code here.
    #

    quit = False
    count = 0
    while not quit:
        A.sort()
        print('k:', k)
        print('len of A:', len(A))
        print('min, max:', min(A), max(A))
        #print('10 first:', [A[i] for i in range(0,10)])

        if pow(3, log(len(A), 2)) * max(A) < k:
            return -1
        if len(A) == 1 and A[0] < k:
            return -1

        smaller = list(filter(lambda x: x<k, A))
        print('len(smaller)', len(smaller))
        #bigger = list(filter(lambda x: x>=k, A))

        if len(smaller) == 0:
            print('len(smaller)==0, RETURN')
            return count

        #if(len(smaller) < len(bigger)):
        #    print('EARLY RETURN')
        #    return len(smaller)  + count
        C = []
        pivot = min(int(len(A)/2), len(smaller))
        for a, b in zip(A[0:pivot], A[pivot:2*pivot]):
            if a > b:
                c = b + 2*a
            else:
                c = a + 2*b
            count+=1
            C.append(c)
        C+=A[2*pivot:]
        #if len(A) % 2 != 0:
        #    C.append(A[-1])
        A = C
        

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
