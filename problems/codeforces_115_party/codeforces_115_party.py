#!/usr/bin/env python3
import sys
from collections import defaultdict, deque

"""
Today the company is going to arrange a party. This involves dividing all n
employees into several groups: every employee must belong to exactly one group.
Furthermore, within any single group, there must not be two employees A and B
such that A is the superior of B.
"""


class Graph:
    def __init__(self):
        self._g = defaultdict(deque)

    def ins_edge(self, v1, v2):
        self._g[v1].append(v2)

    def neighbours(self, vertex):
        if vertex not in self:
            return []
        return self._g[vertex]

    def __repr__(self):
        return repr(self._g)

    def __contains__(self, vertex):
        return vertex in self._g

    def __iter__(self):
        return iter(self._g)

    @classmethod
    def from_edges(cls, edges):
        g = cls()
        for v1, v2, cost in edges:
            g.ins_edge(v1, v2, cost)

        return g


def dfs(g, s):
    path = dict()
    queue = deque()
    discovery_time = 0
    max_depth = 0

    queue.append((s, 0))
    while queue:
        vertex, depth = queue.pop()
        if depth > max_depth:
            max_depth = depth

        if vertex not in path:
            path[vertex] = discovery_time
            discovery_time += 1
            # yield vertex
        for neighbor in g.neighbours(vertex):
            if neighbor not in path:
                queue.append((neighbor, depth + 1))

    return max_depth


def main(rl):
    _n_number_of_employees = int(rl())  # n (1 ≤ n ≤ 2000)

    g = Graph()
    ceo = 0

    for employee in range(1, _n_number_of_employees + 1):
        manager = int(rl())

        if manager == -1:
            manager = ceo
        g.ins_edge(manager, employee)

    max_depth = dfs(g, ceo)
    return max_depth


if __name__ == "__main__":
    rl = sys.stdin.readline
    solution = main(rl)
    print(solution)
