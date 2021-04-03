#!/usr/bin/env python3
"""
Turn the script executable:

> chmod +x ./<name>.py

To turn on optional debug:

> chmod +x ./<name>.py --debug

"""
import sys
from collections import deque

CAN_HANDLE_MSG = ("Nao", "Sim", )

rl = sys.stdin.readline


class Park:

    def __init__(self, k):
        self.k = k
        self.drivers = deque()
        self.can_handle = True

    def add_driver(self, start, end):
        if not self.can_handle:
            return

        last_start, last_end = self._peek
        while last_end and start >= last_end and self.drivers:
            self.drivers.pop()
            last_start, last_end = self._peek

        if len(self.drivers) + 1 > self.k:
            self.can_handle = False
            return

        if not self.drivers or (start >= last_start and end <= last_end):
            self.drivers.append((start, end))
        else:
            self.can_handle = False

    @property
    def _peek(self):
        return self.drivers[-1] if self.drivers else (None, None)


results = []
while True:
    # n, k = drivers (3 ≤ N ≤ 10⁴), max supported cars (1 ≤ K ≤ 10³)
    n, k = map(int, rl().split())

    if n == k == 0:
        break  # empty test case

    schedule = (map(int, rl().split()) for _ in range(n))

    p = Park(k)
    for start, end in schedule:
        p.add_driver(start, end)
    results.append(f"{CAN_HANDLE_MSG[p.can_handle]}")

if results:
    sys.stdout.write("\n".join(results) + '\n')
