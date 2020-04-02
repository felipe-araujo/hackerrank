def test_case_14():
    with open('flatland-space-stations_input14.txt') as f:
        lines = f.readlines()
        nm = lines[0].split()
        n = int(nm[0])
        m = int(nm[1])
        c = list(map(int, lines[1].rstrip().split()))
        return n, m, c
    
def test_case_15():    
     with open('flatland-space-stations_input15.txt') as f:
        lines = f.readlines()
        nm = lines[0].split()
        n = int(nm[0])
        m = int(nm[1])
        c = list(map(int, lines[1].rstrip().split()))
        return n, m, c

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    print('city size:', n)
    print('stations size:', len(c))
    d = 0
    c.sort()
    bounds = [c[0], c[-1]]
    #c = [min(c), max(c)]
    city = 0
    while city < n:
        #print('city:', city)        
        m = n
        for station in c:
        
            dist = city-station
            adist = abs(dist)
            if dist == 0:
                m = 0
                city += max(d-1, 0)
                break
            dist = abs(dist)
            if station < city and dist < d:
                city += max(d-1, 0)            
            if dist < m:
                m = dist            
        if m == 0:
            city +=1
            continue
        elif m > d:
            d = m
        city +=1
    return d

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #nm = input().split()

    #n = int(nm[0])

    #m = int(nm[1])

    #c = list(map(int, input().rstrip().split()))

    n, m, c = test_case_14()
    import time
    t = time.process_time()
    result = flatlandSpaceStations(n, c)
    elapsed_time = time.process_time() - t        
    print('Time elapsed: ', elapsed_time)
    print('Previous time was 12.872039492999999')
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
