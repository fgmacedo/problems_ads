#!/usr/bin/env python3
import sys
from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self._g = defaultdict(set)

    def ins_edge(self, v1, v2):
        self._g[v1].add(v2)
        self._g[v2].add(v1)

    def adjacents(self, vertex):
        if vertex not in self:
            raise ValueError(f"Vertex {vertex} not found in graph.")
        return self._g[vertex]

    def __repr__(self):
        return repr(self._g)

    def __contains__(self, vertex):
        return vertex in self._g

    @classmethod
    def from_edges(cls, edges):
        g = cls()
        for v1, v2 in edges:
            g.ins_edge(v1, v2)

        return g


def dfs(g, start_point):
    l = deque()
    visited = set()
    time = 0

    l.append(start_point)

    while l:
        vertex = l.pop()
        visited.add(vertex)
        for adj in g.adjacents(vertex):
            if adj not in visited:
                time += 1
                l.append(adj)
    return time


if __name__ == "__main__":
    rl = sys.stdin.readline

    number_of_test_cases = int(rl())  # T (T < 100)

    solutions = []
    for _ in range(number_of_test_cases):
        n_start_point = int(
            rl()
        )  # N (N < X2, onde X é a largura em nodos do labirinto, que pode variar de 3 até 7)
        _num_v, num_e = [int(x) for x in rl().split()]  # vertices, arestas

        edges = ([int(x) for x in rl().split()] for _ in range(num_e))

        # build the graph
        g = Graph.from_edges(edges)

        # find the minimun spanning tree
        max_level = dfs(g, n_start_point)

        solution = f"{max_level*2}"
        solutions.append(solution)

    print("\n".join(solutions))
