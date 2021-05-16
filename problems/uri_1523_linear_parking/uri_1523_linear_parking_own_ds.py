#!/usr/bin/env python3
"""
Turn the script executable:

> chmod +x ./<name>.py

"""
import sys

rl = sys.stdin.readline


class Node:
    def __init__(self, v, prev=None, next=None):
        self.v = v
        self._prev = prev
        self._next = next

    def __repr__(self):
        return f"{self.v}"


class DoubleLinkedList:
    _sentinel = object()

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
            node._prev = self.tail
            self.tail = node
        return node

    def popleft(self):
        node = self.head
        if node is None:
            raise IndexError("popleft from an empty linked-list")

        self.size -= 1
        self.head = self.head._next
        return node.v

    def pop(self):
        node = self.tail
        if node is None:
            raise IndexError("pop from an empty linked-list")

        self.size -= 1
        self.tail = node._prev
        if self.tail is not None:
            self.tail._next = None
        else:
            self.head = None
        return node.v

    def get_tail(self, defaut=_sentinel):
        if self:
            return self.tail.v
        elif defaut is self._sentinel:
            raise IndexError("get from an empty linked-list")
        return defaut

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        for idx, value in enumerate(self):
            if idx == index:
                return value
        else:
            raise IndexError("linked-list index out of range")

    def __iter__(self):
        prev = self.head
        while prev:
            yield prev.v
            if prev and prev._next is not None:
                prev = prev._next
            else:
                break

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(repr(no) for no in self)})"


def can_handle(k, schedule):
    CAN_HANDLE_MSG = (
        "Nao",
        "Sim",
    )
    can_handle = True
    park = DoubleLinkedList()
    empty = (None, None)

    for start, end in schedule:
        if not can_handle:
            continue

        last_start, last_end = park.get_tail(empty)
        while last_end and start >= last_end and park:
            park.pop()
            last_start, last_end = park.get_tail(empty)

        if len(park) + 1 > k:
            can_handle = False
            continue

        if not park or (start >= last_start and end <= last_end):
            park.append((start, end))
        else:
            can_handle = False

    return CAN_HANDLE_MSG[can_handle]


results = DoubleLinkedList()
while True:
    # n, k = drivers (3 ≤ N ≤ 10⁴), max supported cars (1 ≤ K ≤ 10³)
    n, k = map(int, rl().split())

    if n == k == 0:
        break  # empty test case

    schedule = (map(int, rl().split()) for _ in range(n))

    results.append(can_handle(k, schedule))

if results:
    sys.stdout.write("\n".join(results) + "\n")
