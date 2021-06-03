#!/usr/bin/env python3
import sys


class Node:
    def __init__(self, data, depth=0):
        self.data = data
        self.depth = depth
        self.left = None
        self.right = None

    @classmethod
    def from_permutation(cls, permutation, insert_fn=None, depth=0):
        if not permutation:
            return

        data_root = max(permutation)
        root_index = permutation.index(data_root)

        data_left, data_right = (
            permutation[0:root_index],
            permutation[root_index + 1 :],
        )

        root = Node(data_root, depth=depth)
        if insert_fn:
            insert_fn(root)
        cls.from_permutation(
            permutation=data_left, insert_fn=root._ins_left, depth=depth + 1
        )
        cls.from_permutation(
            permutation=data_right, insert_fn=root._ins_right, depth=depth + 1
        )

        return root

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
        _n_permutation_len = int(rl())  # n (1 ≤ n ≤ 100) — the length of the permutation
        a_perm = [int(x) for x in rl().split()]  # a1,a2,…,an  — permutation a.

        root = Node.from_permutation(a_perm)
        solution = " ".join(f"{n.depth}" for n in infix(root))
        solutions.append(solution)

    print("\n".join(solutions))
