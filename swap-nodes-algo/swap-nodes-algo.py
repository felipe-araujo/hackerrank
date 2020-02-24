#!/bin/python3

import os
import sys

class Node:
    def __init__(self, info, level=1): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = level
        self.visited = False

    def __str__(self):
        return str(self.info) 

class BinaryTree:
    def __init__(self): 
        self.root = None

    def create_nodes_from_array(self, arr):
        nodes_queue = []
        self.root = Node(1)
        level = 1
        parent = self.root
        for pair in arr:
            level = parent.level + 1
            
            left = Node(pair[0], level) if pair[0]!= -1 else None
            right = Node(pair[1], level) if pair[1]!= -1 else None
            parent.left = left
            parent.right = right

            if left:
                nodes_queue.append(left)
            if right:
                nodes_queue.append(right)
            if nodes_queue:
                parent = nodes_queue.pop(0)    
    
    
    def height(self, node=None):
        if not node:
            node = self.root        
        return max(node.level, \
            self.height(node.left) if node.left else 0, \
            self.height(node.right) if node.right else 0)
    
    # apply f using DFS - this is important, since 
    # using in order traversal may mess up the swaps - if a parent
    # node is target of a swap operation, applying swap in any descendent
    # will produce wrong results
    def apply(self, f, node = None):                
        if node.left:
            self.apply(f, node.left)
        if node.right:
            self.apply(f, node.right)
        f(node)

    def swap_nodes(self, k):
        h = self.height()
        debug('height: ', h)
        swap_levels = list(range(k, h+1, k))
        debug('swap_levels=', swap_levels, ', k=', k)
        def swap(node):
            if node.level in swap_levels:
                debug('swap at level ', node.level)
                debug('swap l=', str(node.left), ', r=', str(node.right))
                temp = node.right
                node.right = node.left
                node.left = temp
                temp = None      
        self.apply(swap, node=self.root)

    def in_order_traversal(self, node=None, acc = []):
        if not node:
            node = self.root
            acc = []
        if node.left:
            self.in_order_traversal(node.left, acc)
        #print(node.info)
        #acc.append(str(node.info)+"("+str(node.level)+")")
        acc.append(node.info)
        if node.right:
            self.in_order_traversal(node.right, acc)
        
        return acc
#
# Complete the swapNodes function below.
#
#def 
def noprint(*args):
    pass
debug = noprint

def swapNodes(indexes, queries):
    #
    # Write your code here.    
    #
    result = []
    debug('indexes: ', indexes)
    debug('-'*10)
    t = BinaryTree()
    t.create_nodes_from_array(indexes)
    debug(t.in_order_traversal())
    debug('-'*10)
    for q in queries:
        t.swap_nodes(int(q))        
        #print(' '.join(map(str, t.in_order_traversal())))
        result.append(t.in_order_traversal())

    return result
    #' '.join(map(str, t.in_order_traversal()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #fptr = sys.stdout

    sys.setrecursionlimit(10000)

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
