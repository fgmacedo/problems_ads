#!/usr/bin/env python3
import sys
from collections import deque, namedtuple
from time import sleep
from operator import attrgetter


get_peek = attrgetter("peek")  # lambda x: x.peek
debug = "--debug" in sys.argv


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



def hanoi_tower_solver(n, o, d, a, expected_moves=0):
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

    minimum_moves = (2 ** n) - 1
    extra_moves = expected_moves - minimum_moves

    if extra_moves < 0:
        print("N")
        exit(0)
    else:
        print("Y")

    is_even = n % 2 == 0

    if is_even:
        pegs = deque([o, a, d])
    else:
        pegs = deque([o, d, a])

    moves = 0
    while len(d) != n:
        if debug: previous_state = repr(pegs)

        # alter between moves of the lower disc or the other possible movement
        if moves % 2 == 0:
            source, destination = pegs[0], pegs[1]
            disc = source.to(destination, logger)
        else:
            source, destination = pegs[0], pegs[2]
            if not source or (destination and source.peek > destination.peek):
                source, destination = destination, source
            disc = source.to(destination, logger)

            # rotate pegs
            pegs.append(pegs.popleft())

        if debug:
            print(f"{moves:0>3} | {previous_state} | {source} -{disc}-> {destination} | {pegs}\r\n       {', '.join(movements)}\r\n")
            sleep(0.2)
        moves += 1

    return movements


rl = sys.stdin.readline
boats, trips = map(int, rl().split())  # n, k

a = Tower('A', range(boats, 0, -1))  # Portugal
b = Tower('B')  # China
c = Tower('C')  # England

movements = hanoi_tower_solver(boats, a, c, b, trips)
print('\n'.join(movements))
