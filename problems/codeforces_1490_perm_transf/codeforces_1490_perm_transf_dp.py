#!/usr/bin/env python3
import sys
from collections import deque

"""
Solution using dynamic programming (interactive solution instead of recursive)
"""


class Node:
    def __init__(self, data, depth=0):
        self.data = data
        self.depth = depth
        self.left = None
        self.right = None

    @classmethod
    def from_permutation(cls, permutation):
        permutations = deque(
            [
                (permutation, None, 0),
            ]
        )
        main_root = None

        while permutations:
            permutation, insert_fn, depth = permutations.popleft()

            data_root = max(permutation)
            root_index = permutation.index(data_root)

            data_left, data_right = (
                permutation[0:root_index],
                permutation[root_index + 1 :],
            )

            root = Node(data_root, depth=depth)
            if main_root is None:
                main_root = root

            if insert_fn:
                insert_fn(root)

            if data_left:
                permutations.append((data_left, root._ins_left, depth + 1))
            if data_right:
                permutations.append((data_right, root._ins_right, depth + 1))

        return main_root

    def _ins_left(self, node):
        self.left = node

    def _ins_right(self, node):
        self.right = node


def infix(node):
    if node is not None:
        yield from infix(node.left)
        yield node
        yield from infix(node.right)


if __name__ == "__main__":
    rl = sys.stdin.readline

    number_of_test_cases = int(rl())  # t (1 ≤ t ≤ 100)

    solutions = []
    for _ in range(number_of_test_cases):
        _n_permutation_len = int(
            rl()
        )  # n (1 ≤ n ≤ 100) — the length of the permutation
        a_perm = [int(x) for x in rl().split()]  # a1,a2,…,an  — permutation a.

        root = Node.from_permutation(a_perm)
        solution = " ".join(f"{n.depth}" for n in infix(root))
        solutions.append(solution)

    print("\n".join(solutions))
