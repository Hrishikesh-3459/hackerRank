#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    cur = head
    while cur:
        if cur.data > data and cur.prev == None:
            node = DoublyLinkedListNode(data)
            node.next = cur
            cur.prev = node
            node.prev = None
            head = node
            return head
        if cur.data > data and cur:
            node = DoublyLinkedListNode(data)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
            return head
        if cur.next == None:
            node = DoublyLinkedListNode(data)
            node.next = None
            node.prev = cur
            cur.next = node
            return head
        cur = cur.next


if __name__ == '__main__':
