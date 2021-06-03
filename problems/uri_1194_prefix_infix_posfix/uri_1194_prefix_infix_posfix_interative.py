#!/usr/bin/env python3
"""
Imprimir uma linha contendo o percurso posfixo da corrente árvore

## Exemplo de Entrada

```
3
3 xYz Yxz
3 abc cba
6 ABCDEF CBAEDF
```

## Exemplo de Saída

```
Yzx
cba
CBEFDA
```
"""
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @classmethod
    def from_iterator(cls, items):
        items = iter(items)
        root = cls(next(items))
        for item in items:
            root.insert(item)
        return root

    @classmethod
    def from_pre_and_infix(cls, prefix, infix, insert_fn=None):
        if not infix:
            return

        if insert_fn is None:
            data_root = prefix[0]
        else:
            indexes = sorted(prefix.index(infix_item) for infix_item in infix)
            data_root = prefix[indexes[0]]

        root_index_on_infix = infix.index(data_root)
        data_left, data_right = (
            infix[0:root_index_on_infix],
            infix[root_index_on_infix + 1 :],
        )

        # print(f"""infix: {infix}\r\nroot: {data_root} (index: {root_index_on_infix}), left: {data_left}, right: {data_right}\r\n\r\n""")

        root = Node(data_root)
        if insert_fn:
            insert_fn(root)

        # TODO: Remove recursion.
        cls.from_pre_and_infix(prefix=prefix, infix=data_left, insert_fn=root._ins_left)
        cls.from_pre_and_infix(
            prefix=prefix,
            infix=data_right,
            insert_fn=root._ins_right,
        )
        return root

    def _ins_left(self, node):
        self.left = node

    def _ins_right(self, node):
        self.right = node


def prefix(node):
    if node is not None:
        yield node
        yield from prefix(node.left)
        yield from prefix(node.right)


def posfix(node):
    if node is not None:
        yield from posfix(node.left)
        yield from posfix(node.right)
        yield node


if __name__ == "__main__":
    rl = sys.stdin.readline

    # number of cases
    number_of_cases = int(rl().strip())

    solutions = []
    for _ in range(number_of_cases):
        _number_of_nodes, s_prefix, s_infix = rl().split()
        tree = Node.from_pre_and_infix(s_prefix, s_infix)
        s = "".join(node.data for node in posfix(tree))
        solutions.append(s)

    print("\n".join(solutions))
