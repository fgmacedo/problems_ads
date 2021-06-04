#!/usr/bin/env python3
import sys
from collections import defaultdict, deque

"""
Map cell can contain:

    A: Water
    X: Stone
    T: Contaminant
"""
WATER = "A"
STONE = "X"
CONTAMINANT = "T"


class Cell:
    def __init__(self, value, row, column):
        self.value = value
        self.row = row
        self.column = column

    def __hash__(self) -> int:
        return hash(self.value) + hash(self.row) + hash(self.column)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, str):
            return self.value == o
        return self.value == o.value and self.row == o.row and self.column == o.column

    def __repr__(self) -> str:
        return f"C({repr(self.value)}, {self.row}, {self.column})"

    def __str__(self) -> str:
        return self.value


class Graph:
    def __init__(self):
        self._g = defaultdict(deque)

    def ins_edge(self, v1, v2):
        self._g[v1].append(v2)
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


def propagation(g):
    """
    Brute forcing here...  I think that a BSF is applicable.
    """
    keep_processing = True
    while keep_processing:
        keep_processing = False
        for vertex in g:
            for adj in g.adjacents(vertex):
                if vertex.value == WATER and adj.value == CONTAMINANT:
                    vertex.value = CONTAMINANT
                    keep_processing = True


if __name__ == "__main__":
    rl = sys.stdin.readline

    solutions = []
    while True:

        n_lines, m_columns = [int(x) for x in rl().split()]

        if n_lines == m_columns == 0:
            break

        map = []
        for row in range(n_lines):
            row_contents = rl().strip()
            map.append(
                [Cell(item, row, column) for column, item in enumerate(row_contents)]
            )

        g = Graph()
        prev_row = None
        for row in map:
            prev_cell = None
            for cell in row:
                if prev_cell:
                    g.ins_edge(prev_cell, cell)
                prev_cell = cell
            if prev_row:
                for above_cell, current_cell in zip(prev_row, row):
                    g.ins_edge(above_cell, current_cell)
            prev_row = row

        propagation(g)

        new_map = []
        for row in map:
            new_map.append("".join(str(cell) for cell in row))
        solutions.append("\n".join(new_map))

    print("\n\n".join(solutions) + "\n")
