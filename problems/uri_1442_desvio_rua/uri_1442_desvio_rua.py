#!/usr/bin/env python3
import sys
from collections import defaultdict, deque
from copy import deepcopy

"""
Este exercício foi bem desafiador. Não consegui encontrar uma solução por conta
própria e recorri a um algorítmo para resolver.

Passei mais de 10 horas trabalhando neste problema, o que é meio frustrante/desconfortante.


O problema ainda está em discernir entre as soluções 1 ou 2:
    A solução ainda está meio força bruta.

    O melhor seria encontrar os vértices que são pontes (descobri na internet) e
    tentar inverter o sentido apenas destes vértices e ver se temos novamente um grafo
    fortemente conectado.
"""


def tarjan(graph):
    """
    Eu não consegui chegar na implementação deste algorítmo por conta própria.
    Pesquisei online e encontrei um paper falando sobre o Tarjan, tentei implementar mas falhei,
    Encontrei esta implementação no Stack Overflow: https://stackoverflow.com/a/62006383/585592

    Ref: https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
    """
    result = []
    stack = []
    low = {}
    call_stack = []
    for v in graph:
        call_stack.append((v, 0, len(low)))
        while call_stack:
            v, pi, num = call_stack.pop()
            if pi == 0:
                if v in low:
                    continue
                low[v] = num
                stack.append(v)
            if pi > 0:
                low[v] = min(low[v], low[graph[v][pi - 1]])
            if pi < len(graph[v]):
                call_stack.append((v, pi + 1, num))
                call_stack.append((graph[v][pi], 0, len(low)))
                continue
            if num == low[v]:
                comp = []
                while True:
                    comp.append(stack.pop())
                    low[comp[-1]] = len(graph)
                    if comp[-1] == v:
                        break
                result.append(comp)
    return result


def dfs(g, s):
    path = set()
    queue = deque()
    queue.append(s)
    while queue:
        vertex = queue.pop()
        if vertex not in path:
            path.add(vertex)
            yield vertex
        for neighbor in g.neighbors(vertex):
            if neighbor not in path:
                queue.append(neighbor)


def find_change_way_solution(g):
    for v1, v2 in g.E:
        # print(f"  removing {v1, v2}")
        new_g = deepcopy(g)
        new_g.remove_edge(v1, v2, directed=True)
        new_g.ins_edge(v2, v1, directed=True)
        if len(tarjan(new_g)) == 1:
            # print("found solution")
            return v1, v2


class Graph:
    def __init__(self):
        self._g = defaultdict(deque)

    def ins_edge(self, v1, v2, directed=False):
        self._g[v1].append(v2)
        if not directed:
            self._g[v2].append(v1)

    def remove_edge(self, v1, v2, directed=False):
        try:
            self._g[v1].remove(v2)
        except ValueError:
            pass

        if not directed:
            try:
                self._g[v2].remove(v1)
            except ValueError:
                pass

    def __getitem__(self, vertex):
        return self._g[vertex]

    def __len__(self):
        return len(self._g)

    def neighbors(self, vertex):
        if vertex not in self:
            return []
        return self._g[vertex]

    def __repr__(self):
        return repr(self._g)

    def __contains__(self, vertex):
        return vertex in self._g

    def __iter__(self):
        return iter(self._g)

    def is_connected(self, directed=False):
        vertexes = self.V
        if not vertexes:
            return False

        origin = vertexes[0]

        new_g = Graph()
        for edge in self.E:
            new_g.ins_edge(*edge, directed=directed)

        path = set(dfs(new_g, origin))
        return len(self) == len(path)

    @property
    def V(self):
        "List of all vertexes"
        return list(iter(self))

    @property
    def E(self):
        "List of all edges"
        return [
            (vertex, neighbor)
            for vertex, neighbors in self._g.items()
            for neighbor in neighbors
        ]


def main(rl):
    solutions = []
    while True:
        new_test_case = rl().strip()
        if not new_test_case:
            break

        # n (1 ≤ N ≤ 10^3)  número de cruzamentos
        # m (1 ≤ M ≤ 10^5)  número de ruas da cidade
        _n_crossings, m_streets = [int(x) for x in new_test_case.split()]

        digraph = Graph()
        graph = Graph()
        blocked_street = None
        for _m_number in range(m_streets):
            street_def = rl().strip()
            # A (1 ≤ A), B (B ≤ N) e T (1 ≤ T ≤ 2)
            # T: Direction, 1 directed from A -> B, 2 both sides A <-> B
            a_origin, b_dest, t_direction = [int(x) for x in street_def.split()]
            if blocked_street is None:
                blocked_street = (a_origin, b_dest)
            digraph.ins_edge(a_origin, b_dest, directed=t_direction == 1)
            graph.ins_edge(a_origin, b_dest, directed=False)

        digraph.remove_edge(*blocked_street)
        graph.remove_edge(*blocked_street)

        strongly_connected_components = tarjan(digraph)
        if len(strongly_connected_components) == 1:
            solution = "-"
        elif not graph.is_connected():
            solution = "*"
        else:
            edge = find_change_way_solution(digraph)
            if edge:
                solution = "1"
            else:
                solution = "2"

        solutions.append(solution)

    return "\n".join(solutions)


if __name__ == "__main__":
    rl = sys.stdin.readline
    solutions = main(rl)
    print(solutions)
