#!/usr/bin/env python3
import sys
from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self._g = defaultdict(set)

    def ins_edge(self, v1, v2):
        self._g[v1].add(v2)
        self._g[v2].add(v1)

    def neighbors(self, vertex):
        if vertex not in self:
            # print(f"  {vertex} not in {self}")
            return []
        return self._g[vertex]

    def __repr__(self):
        return repr(self._g)

    def __contains__(self, vertex):
        return vertex in self._g

    @property
    def V(self):
        "List of all vertexes"
        return list(self._g.keys())


def bfs(g, s, max_level):
    visited = set()
    queue = deque()

    queue.append((s, 0))
    visited.add(s)
    while queue:
        vertex, vertex_level = queue.popleft()
        if vertex_level > max_level:
            break
        yield vertex
        vertex_level += 1
        for adj in g.neighbors(vertex):
            if adj not in visited:
                queue.append((adj, vertex_level))
                visited.add(adj)


def pairs(iterable):
    return zip(*[iter(iterable)] * 2)


if __name__ == "__main__":
    rl = sys.stdin.readline

    solutions = []
    case_no = 1
    while True:
        line = rl()
        if line.strip() == "":
            continue

        _number_of_connections = int(line)  # T (T < 100)
        if not _number_of_connections:
            break

        g = Graph()

        conn_count = 0
        while conn_count < _number_of_connections:
            line = rl()
            lazy_connections = (int(x) for x in line.split())

            for pair in pairs(lazy_connections):
                conn_count += 1
                g.ins_edge(*pair)

        num_vertices = len(g.V)

        null_query_found = False
        while not null_query_found:
            line = rl()
            lazy_queries = (int(x) for x in line.split())
            queries = list(pairs(lazy_queries))

            for start_node, depth in queries:
                if start_node == depth == 0:
                    null_query_found = True
                    break

                reached_nodes = list(bfs(g, start_node, depth))
                not_reached = num_vertices - len(reached_nodes)
                solution = f"Case {case_no}: {not_reached} nodes not reachable from node {start_node} with TTL = {depth}."
                solutions.append(solution)
                case_no += 1

    print("\n".join(solutions))
