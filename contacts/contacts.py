#!/bin/python3

import os
import sys

class TrieNode:
    def __init__(self, data):
        self.data = data
        self.terminal = False
        self.children = []
        self.counter = 1

    def search_children(self, c):
        for child in self.children:
            if child.data == c:
                return child
        return None
    def increment(self):
        self.counter = self.counter + 1
    def zero(self):
        self.counter = 0

    def count_leafs(self):
        return self.counter# + 1 if self.terminal else self.counter

class Trie:
    def __init__(self):
        self.root = TrieNode(None)
        self.root.zero()

    def add(self, word):
        current_node = self.root
        for c in list(word):
            node = current_node.search_children(c)
            if node:
                node.increment()                 
                current_node = node
                continue
            else:
                new_node = TrieNode(c)
                current_node.children.append(new_node)
                current_node = new_node
                continue
        current_node.terminal = True
        
    def __str__(self):
        return str(self.root)
    
    def starts_with(self, expression):
        current_node = self.root
        for c in list(expression):
            node = current_node.search_children(c)
            if node:
                current_node = node
                continue
            else:
                return 0 # no one matches
        return current_node.count_leafs()

#
# Complete the contacts function below.
#
book = Trie()
def contacts(queries):
    result = []
    for args in queries:
    
        if args[0] == 'add':
            book.add(args[1])
            #print(book)
        else:
            result.append(book.starts_with(args[1]))
    return result
    #
    # Write your code here.
    #

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
