#!/usr/bin/env python3
"""
Turn the script executable:

> chmod +x ./<name>.py
"""
import sys

rl = sys.stdin.readline
number_of_testcases = int(rl())


class Node:
    def __init__(self, v, next=None):
        self.v = v
        self._next = next

    def __repr__(self):
        return f"{self.v}"


class LinkedList:
    def __init__(self, head=None):
        self.size = 0
        self.head = head
        self.tail = head

    def append(self, v):
        self.size += 1
        node = Node(v)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail._next = node
            self.tail = node
        return node

    def popleft(self):
        node = self.head
        if node is None:
            raise IndexError("pop from an empty linked-list")

        self.size -= 1
        self.head = self.head._next
        return node.v

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        for idx, node in enumerate(self):
            if idx == index:
                return node.v
        else:
            raise IndexError("linked-list index out of range")

    def __iter__(self):
        prev = self.head
        while prev:
            yield prev
            if prev and prev._next is not None:
                prev = prev._next
            else:
                break

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(repr(no) for no in self)})"


for _ in range(number_of_testcases):
    # l: the size in meters of the ferry (1 ≤ l ≤ 500)
    # m: number of cars (1 ≤ m ≤ 10000)
    l, m = map(int, rl().split())

    number_of_cars = m
    ferry_size = l * 100

    banks = LinkedList(), LinkedList()
    insert = [b.append for b in banks]
    for _ in range(number_of_cars):
        length, destiny = rl().split()
        insert[destiny != "left"](int(length))

    iterations = 0
    while any(banks):
        occuped_space = 0
        bank = banks[iterations % 2]
        while bank and occuped_space + bank[0] <= ferry_size:
            occuped_space += bank.popleft()
        iterations += 1

    print(iterations)
