#!/usr/bin/env python3
import sys
from collections import deque
from itertools import cycle
from time import sleep
from operator import attrgetter


get_peek = attrgetter("peek")  # lambda x: x.peek



class Tower:

    def __init__(self, name: str, discs=None):
        self.name = name
        self._discs = deque(discs or [])
        self._push = self._discs.append
        self._pop = self._discs.pop

    def empty(self):
        return not bool(self._discs)

    def __len__(self):
        return len(self._discs)

    @property
    def peek(self):
        try:
            return self._discs[-1]
        except IndexError:
            return 0

    def to(self, other, logger):
        if self.empty():
            return
        other_peek = other.peek
        if  other_peek and other_peek < self.peek:
            # print(f"invalid movement: {self.name} {other.name}")
            return
        disc = self._pop()
        other._push(disc)
        logger(f"{self.name} {other.name}")
        return disc

    @property
    def discs(self):
        return list(self._discs)

    def __repr__(self):
        return f"{self.name}({' '.join(str(x) for x in self._discs)})"



def hanoi_tower_solver(o, d, a, extra_moves=0):
    """
    Rules:
    1. Move only one disc at time.
    2. Cannot have a greater disc above a smaller one.

    Args:
        n: Number of discs
        o: Origin
        d: Destiny
        a: Aux

    """
    movements = []
    logger = movements.append
    pegs = [o, d, a]
    pegs_len = len(pegs)

    n = len(o)
    is_even = n % 2 == 0
    # print(f"is_even: {is_even}")

    if is_even:
        pegs = [o, a, d]
        d, a = a, d

    i = 0
    while extra_moves > 0:
        # print(f"{i:0>3}","extra", o, d, a, extra_moves, ', '.join(movements))
        iteration = i % 3
        if iteration == 0:
            o.to(d, logger)
        elif iteration == 1:
            d.to(o, logger)
        else:
            o.to(a, logger)

        extra_moves -= 1
        i += 1

    last_was_one = False
    if a.peek == 1:
        a.to(b, logger)
        last_was_one = True

    index_of_one = [x.peek for x in pegs].index(1)

    def move_only_possible():
        pegs_sorted = sorted((x for x in pegs if x.peek), key=get_peek)
        source = pegs_sorted[1]
        for peg in pegs:
            if peg != source and not peg.peek == 1:
                dest = peg
        print(f"  move_only_possible: {source} to {dest}")
        source.to(dest, logger)

    def move_one():
        next_index = (index_of_one + 1) % pegs_len
        source = pegs[index_of_one]
        dest = pegs[next_index]
        print(f"  move_one: {source} to {dest}")
        source.to(dest, logger)
        return next_index

    while (len(d) < n and not is_even) or (len(a) < n and is_even):
        print(f"{i:0>3} - {pegs} - {', '.join(movements)}")
        if last_was_one:
            move_only_possible()
            last_was_one = False
        else:
            index_of_one = move_one()
            last_was_one = True

        i += 1
        sleep(0.3)

    return movements

rl = sys.stdin.readline
boats, trips = map(int, rl().split())  # n, k

needed_moves = (2 ** boats) - 1
extra_moves = trips - needed_moves
if extra_moves < 0:
    print("N")
    exit(0)

a = Tower('A', reversed(range(1, boats+1)))  # Portugal
b = Tower('B')  # China
c = Tower('C')  # England

print("Y")
mov_hanoi = hanoi_tower_solver(a, c, b, extra_moves)
print('\n'.join(mov_hanoi))
