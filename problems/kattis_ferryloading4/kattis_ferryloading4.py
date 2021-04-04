#!/usr/bin/env python3
"""
Turn the script executable:

> chmod +x ./<name>.py
"""
import sys
from collections import deque

rl = sys.stdin.readline
number_of_testcases = int(rl())

solutions = deque()
for _ in range(number_of_testcases):
    # l: the size in meters of the ferry (1 ≤ l ≤ 500)
    # m: number of cars (1 ≤ m ≤ 10000)
    l, m = map(int, rl().split())

    number_of_cars = m
    ferry_size = l * 100

    banks = deque(), deque()
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

    solutions.append(iterations)

print("\n".join(map(str, solutions)))
