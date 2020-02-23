#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):

    # if anyone has moved more than 2 positions ahead, it is not possible
    # to have achieved such configuration while maintaining accordance with the
    # given rules, so we print 'too chaotic'.
    # (enumerate starts with index 0)
    diffs = [orig_pos - (new_pos + 1) for (new_pos, orig_pos) in enumerate(q)]
    if len(list(filter(lambda t: t > 2, diffs))) > 0:
        print('Too chaotic')
        return
    
    # 3 2 1
    # 1 2 3
    # 0 1 2

    # account for all elements that have bribed and ended in a better position
    # and remove them from the list
    minimum = (sum(list(filter(lambda t: t>0, diffs))))
    
    q = [v for (pos, v) in enumerate(q) if v<=(pos+1)]
    
    #return

    # new list only with elements have changed positions. 
    # this is the case for one element that has bribed and has also been bribed
    q = [normal for (normal, ordered) in zip(q, sorted(q)) if normal!=ordered ]

    bribes = {position: bribes for position, bribes in zip(sorted(q), [0]*len(q))}
    #minimum += 2*len(q)
    while q:
        try:
            #q = reverse_bribe(q, min(q), bribes)
            q = reverse_bribe_3(q, bribes)
        except ValueError:
            print('Too chaotic')
            return
    #print('Final bribes:', bribes)
    #print('Final q:', q)
    minimum += sum(bribes.values())
    print(minimum)

def reverse_bribe(q, pivot, bribes):
    """ Pivot is always the lowest element in the array.
    We keep moving it until it reaches its natural position, at which point
    we need only to reorder the remaining of the array.
    We must keep track of how many bribes each pearson in the queue has already given.

    2 3 4 5 1
    """
    if not q:
        return q
    if(q[0]) == pivot:
        return q[1:]
    else:
        idx = q.index(pivot)
        for i in range(0, idx):
            if bribes[q[i]] >= 2:
                raise ValueError('Too chaotic')
            else:
                bribes[q[i]] += 1
        q.remove(pivot)
        return q
            
def reverse_bribe_2(q, bribes):
    while len(q) > 1:
        if q[0] > q[1]:
            if bribes[q[0]] >= 2:
                raise ValueError('Too chaotic')
            else:
                bribes[q[0]] +=1
                q = [q[0]] + q[2:]
        else:
            q = q[1:]
    return None

def reverse_bribe_3(q, bribes):
    qsort = sorted(q)
    for pivot in qsort[0:-1]:
        if(q[0]) == pivot:
            q = q[1:]
        else:
            idx = q.index(pivot)
            for i in range(0, idx):
                if bribes[q[i]] >= 2:
                    raise ValueError('Too chaotic')
                else:
                    bribes[q[i]] += 1
            q.remove(pivot)
            #return q
    return None


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
