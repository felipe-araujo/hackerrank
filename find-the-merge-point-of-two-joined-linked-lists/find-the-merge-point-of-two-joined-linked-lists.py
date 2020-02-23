#!/bin/python3

import math
import os
import random
import re
import sys

def test_case04():
    with open('find-the-merge-point-of-two-joined-linked-lists-input02.txt') as f:
        lines  = f.readlines()
        i = 0
        tests = int(lines[i])
        i +=1

        for tests_itr in range(tests):
            index = int(lines[i])
            i+=1

            llist1_count = int(lines[i])
            i+=1

            llist1 = SinglyLinkedList()

            for _ in range(llist1_count):
                llist1_item = int(input())
                llist1.insert_node(llist1_item)
                
            llist2_count = int(input())

            llist2 = SinglyLinkedList()

            for _ in range(llist2_count):
                llist2_item = int(input())
                llist2.insert_node(llist2_item)
                
            ptr1 = llist1.head;
            ptr2 = llist2.head;

            for i in range(llist1_count):
                if i < index:
                    ptr1 = ptr1.next
                    
            for i in range(llist2_count):
                if i != llist2_count-1:
                    ptr2 = ptr2.next

            ptr2.next = ptr1

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    #merge = None
    node1 = head1
    node2 = head2

    if node1.next == node2:
        return node2.data
    if node2.next == node1:
        return node1.data

    while node1:
        node2 = head2
        if node1 == node2:
            print('e pode isso?')
        while node2:
            if node1.next and node2.next and (node1.next == node2.next):
                return node1.next.data
            node2 = node2.next
            if node1 == node2:
                return node1.data
        node1 = node1.next
    print('\n---------\n')
    print_singly_linked_list(head1, ' ', sys.stdout)
    print('\n')
    print_singly_linked_list(head2, ' ', sys.stdout)
    print('\n---------\n')
    return -1

if __name__ == '__main__':
    fptr = sys.stdout

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)
            
        ptr1 = llist1.head;
        ptr2 = llist2.head;

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()