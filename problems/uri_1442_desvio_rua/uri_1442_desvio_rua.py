#!/usr/bin/env python3
import sys
from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self._g = defaultdict(deque)

    def ins_edge(self, v1, v2, directed=False):
        self._g[v1].append(v2)
        if not directed:
            self._g[v2].append(v1)

    def adjacents(self, vertex):
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
        for v1, v2 in edges:
            g.ins_edge(v1, v2)

        return g


def main(rl):
    solutions = []
    while True:

        new_test_case = rl().strip()
        if not new_test_case:
            break

        # n (1 ≤ N ≤ 10^3)  número de cruzamentos
        # m (1 ≤ M ≤ 10^5)  número de ruas da cidade
        n_crossings, m_streets = [int(x) for x in new_test_case.split()]


        g = Graph()
        for _m_number in range(m_streets):
            street_def = rl().strip()
            # A (1 ≤ A), B (B ≤ N) e T (1 ≤ T ≤ 2)
            # T: Direction, 1 directed from A -> B, 2 both sides A <-> B
            a_origin, b_dest, t_direction = [int(x) for x in street_def.split()]
            g.ins_edge(a_origin, b_dest, directed=t_direction == 1)


        # TODO: Solution goes here :)

        solutions.append(f"{g!r}")

    return "\n\n".join(solutions) + "\n"



if __name__ == "__main__":
    rl = sys.stdin.readline
    solutions = main(rl)
    print(solutions)

