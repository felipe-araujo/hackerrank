def test_case06():
    data = []
    with open('merge-two-sorted-linked-lists-input06.txt') as f:
        lines = f.readlines()
        tests = int(lines[0])
        i = 1
        for tests_itr in range(tests):
            llist1_count = int(lines[i])
            i+=1

            llist1 = SinglyLinkedList()

            for _ in range(llist1_count):
                llist1_item = int(lines[i])
                i+=1
                llist1.insert_node(llist1_item)
                
            llist2_count = int(lines[i])
            i+=1

            llist2 = SinglyLinkedList()

            for _ in range(llist2_count):
                llist2_item = int(lines[i])
                i +=1
                llist2.insert_node(llist2_item)
            data.append((llist1, llist2))
        return data



#!/bin/python3

import math
import os
import random
import re
import sys

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

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    if not head1 and not head2:
        return head1
    if head1 and not head2:
        return head1
    if head2 and not head1:
        return head2

    p1 = head1
    p2 = head2
    head = None
    
    if p1.data < p2.data:
        head = p1
        current = head
        p1 = p1.next
    else:
        head = p2
        current = head
        p2 = p2.next
    
    while p1 or p2:
        if not p1 and p2:
            #current.next = p2
            #current = p2
            break
        if not p2 and p1:
            #current.next = p1
            #current = p1
            break

        if p1.data == p2.data:
            temp1 = p1.next
            temp2 = p2.next
            
            current.next = p1
            p1.next = p2
            current = p2
            
            p1 = temp1
            p2 = temp2
        elif p1.data < p2.data:
            temp = p1.next
            current.next = p1
            current = p1
            p1 = temp
        else:
            temp = p2.next
            current.next = p2
            current = p2
            p2 = temp
    #current.next = None
    return head
        


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #tests = int(input())
    data = test_case06()
    for llist1, llist2 in data:
    #    llist1_count = int(input())

        #llist1 = SinglyLinkedList()

        #for _ in range(llist1_count):
        #    llist1_item = int(input())
        #    llist1.insert_node(llist1_item)
            
        #llist2_count = int(input())

        #llist2 = SinglyLinkedList()

        #for _ in range(llist2_count):
        #    llist2_item = int(input())
        #    llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', sys.stdout)
        print()
        #fptr.write('\n')

    #fptr.close()
