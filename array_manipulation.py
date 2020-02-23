#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation00(n, queries):
    partials = []
    for target in range(0, len(queries)):
        #result = 
        start = queries[target][0]
        end = queries[target][1]
        current = [queries[target][2]] * (end-start+1)
        for t in range(0, len(queries)):
            if target == t:
                continue
            q = queries[t]
            if start > q[1] or end < q[0]:
                continue
            # exact coincidence
            if start == q[0] and end == q[1]:
                current = [x+q[2] for x in current]
                continue
            l0 = max(start, q[0]) - start
            l1 = min(end, q[1]) - start + 1
            current[l0:l1] = [x+q[2] for x in current[l0:l1]]
        print('current:', current)
        print('len(current): ', len(current))
        partials.append(max(current))
    return max(partials)

def arrayManipulation(n, queries):
    # ordena pelo fim de cada query
    queries.sort(key = lambda x: x[1])    
    if should_print:
        print('finished sorting')
        print('first query: ', queries[0])
        print('last query: ', queries[-1])
        print('\nall queries: ', queries, '\n')
    end = queries[-1][0] - 1
        
    return max_subarray(n, 0, queries)

def query_within_limits(q, start, end):
    if q[0] > start and q[0] <=end:
        return True
    if q[1] > start and q[1] <=end:
        return True    
    return False
def query_takes_all_interval(q, start, end):
    if q[0] <= start and q[1]>end:
        return True
    else:
        return False

should_print = False
def max_subarray(size_of_array, offset, queries, limit = None):

    if not queries:
        return 0

    if not limit:
        limit = max(map(lambda x:x[2], queries))
        #print('upper limit:', limit)
    
    if size_of_array < 100:

        if queries and queries[-1][1] < (offset + size_of_array):            
            diff = (offset + size_of_array) - queries[-1][1]
            if should_print:
                print('reducing size of array by: ', diff)
            size_of_array -= diff

        arr = [0] * size_of_array
        if should_print:
            print('offset:', offset)
            print('queries', list(queries))
            print('arr', arr)
            print('will start iterate over queries. len = ', len(list(queries)))
        for q in list(queries):
            if should_print:
                print('q:', q)
            # starts, ends or lies within?
            lbound = (q[0]-offset-1)
            if lbound < 0:
                lbound = 0
            #lbound = min(0, lbound)
            ubound = (q[1]-offset)
            if ubound > size_of_array:
                ubound = size_of_array
            #ubound = min(size_of_array, ubound)
            if should_print:
                print('lbound, ubound: ', lbound, ubound)
                print('arr[lbound:ubound]', arr[lbound:ubound])
            arr[lbound:ubound] = [x+q[2] for x in arr[lbound:ubound]]
            if should_print:
                print('[2] - arr[lbound:ubound]', arr[lbound:ubound])
                print('arr', arr, '\n')
        return max(arr)
    else:
        size_01 = int(size_of_array/2)
        size_02 = size_of_array - size_01
        offset_01 = offset
        offset_02 = offset + size_01

        q1 = list(filter(lambda x: query_within_limits(x, offset_01, offset_01+size_01), queries))
        q2 = list(filter(lambda x: query_within_limits(x, offset_02, offset_02+size_02), queries))
        q_both1 = list(filter(lambda x: query_takes_all_interval(x, offset_01, offset_01+size_01), queries))
        q_both2 = list(filter(lambda x: query_takes_all_interval(x, offset_02, offset_02+size_02), queries))
        

        if q1 and q1[-1][1] < (offset_01 + size_01):
            diff = (offset_01 + size_01) - q1[-1][1]
            #print('reducing size of array 01 by: ', diff)
            size_01 -= diff

        if q2 and q2[-1][1] < (offset_02 + size_02):
            diff = (offset_02 + size_02) - q2[-1][1]
            #print('reducing size of array 02 by: ', diff)
            size_02 -= diff

        c1 = list(map(lambda x: x[2], q_both1))
        if should_print:
            print('queries for all interval c1: ', c1)
        c1 = sum(c1)
        if should_print:
            print('c1: ', c1)

        c2 = list(map(lambda x: x[2], q_both2))
        if should_print:
            print('queries for all interval c2: ', c2)
        c2 = sum(c2)
        if should_print:
            print('c: ', c2)

        if should_print: #or offset < 10:
            print('split array of size ', size_of_array, 'offset: ', offset, ' into 2:')
            print('arr1: size: ', size_01, ' offset:', offset_01)
            print('arr5: size: ', size_02, ' offset:', offset_02, '\n')
        
        old_limit =limit
        limit = max(limit, c1, c2)
        #if old_limit != limit:
            #print('limit updated: ', limit)
        if sum(map(lambda x: x[2], q1)) + c1 < limit:
            max1 = 0
            #print('\n***using limit on 1')
        else:
            max1 = max_subarray(size_01, offset_01, q1, c2) + c1
        
            #limit  = max(max1, limit)
        
        if sum(map(lambda x: x[2], q2)) + c2 < limit:
            #print('\n***using limit on 2')
            max2 = 0
        else:
            max2 = max_subarray(size_02, offset_02, q2, c1) + c2

        #max1 = max_subarray(size_01, offset_01, q1) + c1
        #max2 = max_subarray(size_02, offset_02, q2) + c2
        if limit < max(max1, max2):
            limit = max(max1, max2)
        return max(max1, max2)



def test_case_13():
    with open('arr_manipu_13.txt') as f:
        lines = f.readlines()
        nm = lines[0].split()
        n = int(nm[0])
        m = int(nm[1])
        queries = []
        for l in lines[1:]:
            queries.append(list(map(int, l.rstrip().split())))
    return n, queries

def test_case_0():
    n, m = 5, 3
    queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    return n, queries

def test_case_01():
    n = 10
    queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
    return n, queries



if __name__ == '__main__':
    
    #nm = input().split()

    n, queries = test_case_0()

    print('Got ', len(queries), ' queries, n=', n)

    result = arrayManipulation(n, queries)
    print('\n\t---   result: ', result)
    print('\t--- expected: ', 200)

    n, queries = test_case_01()

    print('Got ', len(queries), ' queries, n=', n)

    result = arrayManipulation(n, queries)
    print('\n\t---   result: ', result)
    print('\t--- expected: ', 10)

    if True:
        queries = []
        n, queries = test_case_13()

        print('Got ', len(queries), ' queries, n=', n)
        import time
        t = time.process_time()
        result = arrayManipulation(n, queries)

        elapsed_time = time.process_time() - t
        print('Time elapsed: ', elapsed_time)
        print('Previous time was ~ 15.5s')


        print('\n\t---   result: ', result)
        print('\t--- expected: ', 2490686975)

    
