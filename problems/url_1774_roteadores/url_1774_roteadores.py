#!/usr/bin/env python3
import sys
from collections import defaultdict, deque


class Heap:
    """
    Min-value heap.
    """

    def __init__(self, iterable=None):
        self._heap = []
        for value in iterable or []:
            self.push(value)

    def __len__(self):
        return len(self._heap)

    def __repr__(self):
        return repr(self._heap)

    def __getitem__(self, aslice):
        return self._heap[aslice]

    def push(self, value):
        """
        Adds a value to the heap
        """
        self._heap.append(value)
        self._moves_last_value_up()

    def pop(self):
        """
        Return the smallest value.
        Last value goes to the top and moves down until we find it's place
        """
        last_value = self._heap.pop()
        if self._heap:
            return_value = self._heap[0]
            self._heap[0] = last_value
            self._moves_root_down()
            return return_value
        return last_value

    def _moves_last_value_up(self):
        """
        Updates the heap moving the value position to the root until a lower value is found.
        As the heap is already in crescent order, only the last index may be in
        the wrong position.
        """
        root = 0
        position = len(self._heap) - 1
        new_value = self._heap[position]
        while position > root:
            parent_position = (
                position - 1
            ) // 2  # parent is at the half value (binary tree)
            parent_value = self._heap[parent_position]
            if new_value < parent_value:
                # change positions
                self._heap[position] = parent_value
                position = parent_position
            else:
                break
        self._heap[position] = new_value

    def _moves_root_down(self):
        """
        Updates the heap moving the root value down replacing positions by it's smallest
        child until it finds a greater value.
        """
        end_position = len(self)
        position = 0
        new_value = self._heap[position]
        child_position = 2 * position + 1  # child is at the double of value + 1
        while child_position < end_position:
            # find the smaller value between childs
            right_child_position = child_position + 1
            if right_child_position < end_position:  # the right is reachable
                if self._heap[right_child_position] < self._heap[child_position]:
                    child_position = right_child_position

            if self._heap[child_position] > new_value:
                break

            self._heap[position] = self._heap[child_position]
            position = child_position
            self._heap[child_position] = new_value
            child_position = 2 * position + 1


class Graph:
    def __init__(self):
        self._g = defaultdict(deque)

    def ins_edge(self, v1, v2, cost=0):
        if not v1 or not v2:
            return
        self._g[v1].append((v2, cost))
        self._g[v2].append((v1, cost))

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


def mst_cost(graph):
    total_cost = 0
    mst = Graph()
    start = next(iter(graph))
    unexplored = Heap([(0, start, None)])
    while unexplored:
        cost, vertex, parent = unexplored.pop()
        if vertex not in mst:
            mst.ins_edge(parent, vertex, cost)
            total_cost += cost
            for neighbour, cost in graph.neighbours(vertex):
                if neighbour not in mst:
                    unexplored.push((cost, neighbour, vertex))
    return mst, total_cost


def main(rl):
    _r_num_routers, c_num_cables = [int(x) for x in rl().split()]

    g = Graph.from_edges(
        [int(x) for x in rl().split()]
        for _ in range(c_num_cables)
    )

    mst, cost = mst_cost(g)

    return f"{cost}"


if __name__ == "__main__":
    rl = sys.stdin.readline
    solutions = main(rl)
    print(solutions)
