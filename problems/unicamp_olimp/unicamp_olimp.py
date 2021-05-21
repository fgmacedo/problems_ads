#!/usr/bin/env python3
"""
Turn the script executable:

> chmod +x ./<name>.py
"""
import sys
from collections import deque

rl = sys.stdin.readline

# número de países (1 ≤ N ≤ 100), número de modalidades (1 ≤ M ≤ 100)
n, m = map(int, rl().split())

countries = {
    cno: [0, 0, 0, n+1-cno, cno]
    for cno in range(1, n+1)
}

for _ in range(m):
    # o, p, b = ouro, prata, bronze
    o, p, b = map(int, rl().split())
    countries[o][0] += 1
    countries[p][1] += 1
    countries[b][2] += 1

solution = [l for l in sorted(countries.values(), reverse=True)]

print(" ".join([str(l[-1]) for l in solution]))
