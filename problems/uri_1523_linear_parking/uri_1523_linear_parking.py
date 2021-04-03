#!/usr/bin/env python3
"""
Turn the script executable:

> chmod +x ./<name>.py

"""
import sys
from collections import deque

rl = sys.stdin.readline


def can_handle(k, schedule):
    CAN_HANDLE_MSG = ("Nao", "Sim", )
    can_handle = True
    park = deque()

    for start, end in schedule:
        if not can_handle:
            continue

        last_start, last_end = _peek(park)
        while last_end and start >= last_end and park:
            park.pop()
            last_start, last_end = _peek(park)

        if len(park) + 1 > k:
            can_handle = False
            continue

        if not park or (start >= last_start and end <= last_end):
            park.append((start, end))
        else:
            can_handle = False

    return CAN_HANDLE_MSG[can_handle]


def _peek(park):
    return park[-1] if park else (None, None)


results = []
while True:
    # n, k = drivers (3 ≤ N ≤ 10⁴), max supported cars (1 ≤ K ≤ 10³)
    n, k = map(int, rl().split())

    if n == k == 0:
        break  # empty test case

    schedule = (map(int, rl().split()) for _ in range(n))

    results.append(
        can_handle(k, schedule)
    )

if results:
    sys.stdout.write("\n".join(results) + '\n')
