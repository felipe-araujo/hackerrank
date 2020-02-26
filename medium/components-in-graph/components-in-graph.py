#!/bin/python3

import os
import sys


def noprint(*args):
    pass
debug = noprint


#
# Complete the componentsInGraph function below.
#
def componentsInGraph(gb):
    #
    # Write your code here.
    #
    graph = dict()
    unique_starting_points = set()
    for edge in gb:        
        debug('edge:', edge)
        if edge[0] not in graph:
            graph[edge[0]] = set()
        graph[edge[0]].add(edge[1])
        
        unique_starting_points.add(edge[0])

        if edge[1] not in graph:
            graph[edge[1]] = set()
        graph[edge[1]].add(edge[0])

    debug(graph)
    debug('unique search starting points: ', len(unique_starting_points))

    #debug(dfs(graph, 2, set(), 0))
    #sys.exit(0)
    global_visited = set()
    skipped = list()
    upper, lower = None, None
    for edge in unique_starting_points:
        if edge in global_visited:
            debug('skipping ', edge, ' as it has already been visited somewhat')
            skipped.append(edge)
            continue
        count = dfs(graph, edge, set(), 0, global_visited)
        if not upper or upper < count:
            upper = count
        if not lower or lower > count:
            lower = count
    debug('skipped ', len(skipped), ' computations')
    return [lower, upper]
        
    
def dfs(graph, node, visited, count, global_visited):
    if node not in visited:
        debug('increment at node ', node)
        count += 1
        visited.add(node)
        global_visited.add(node)
    for other_node in graph[node]:
        if other_node in visited:
            continue
        else:
            visited.add(other_node)
            global_visited.add(other_node)
            #count += 1
            t  = dfs(graph, other_node, visited, 1, global_visited)
            debug('dfs returned ', t, ' at node ', other_node)
            count += t
    return count



if __name__ == '__main__':
    sys.setrecursionlimit(40000)
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
