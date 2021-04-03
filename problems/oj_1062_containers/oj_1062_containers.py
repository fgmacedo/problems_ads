#!/usr/bin/env python3
"""
Turn the script executable:

> chmod +x ./<name>.py
"""
import sys
from collections import deque

rl = sys.stdin.readline


def handle(containers):
    stacks = deque()
    for ship in containers:
        for stack in stacks:
            if ship <= stack[-1]:
                stack.append(ship)
                break
        else:  # for's else is only executed if the loop finishes without a break statement
            stacks.append(deque([ship]))

    return len(stacks)


results = [
    f"Case {idx}: {handle(case.rstrip())}"
    for idx, case in enumerate(sys.stdin, 1)
    if not case == "end\n"
]

print("\n".join(results))
