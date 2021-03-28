#!/usr/bin/env python3
import sys
from collections import deque, namedtuple
from time import sleep
from operator import attrgetter


get_peek = attrgetter("peek")  # lambda x: x.peek
debug = "--debug" in sys.argv

"""
Turn the scritp executable
"""

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
            if debug: print(f"  empty tower: {self} to {other.name}")
            return
        other_peek = other.peek
        if  other_peek and other_peek < self.peek:
            if debug: print(f"  invalid movement: {self} {other}")
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

    if debug: ref_pegs = list(pegs)

    moves = 0
    while len(d) != n or extra_moves:
        if debug: previous_state = repr(ref_pegs)
        move_smallest_disc = moves % 2 == 0

        if extra_moves:
            # overpriced contract, need to expend the money anyway
            symmetric_moves = extra_moves // 2
            odd_extra_move = extra_moves % 2

            if debug: print(f"extra_moves: {extra_moves}, symmetric_moves:{symmetric_moves}, odd_extra_move:{odd_extra_move}")

            for _ in range(symmetric_moves):
                source, destination = pegs[0], pegs[1]
                disc = source.to(destination, logger)
                if debug:
                    print(f"{moves:0>3} EXTRA SYM{_} | {previous_state} | {source} -{disc}-> {destination} ({move_smallest_disc}) | {ref_pegs}\r\n       {', '.join(movements)}\r\n")
                    previous_state = repr(ref_pegs)
                moves += 1
                source, destination = destination, source
                disc = source.to(destination, logger)
                if debug:
                    print(f"{moves:0>3} EXTRA SYM{_} | {previous_state} | {source} -{disc}-> {destination} ({move_smallest_disc}) | {ref_pegs}\r\n       {', '.join(movements)}\r\n")
                    previous_state = repr(ref_pegs)
            if odd_extra_move:
                source, destination = pegs[0], pegs[2]
                disc = source.to(destination, logger)

                # we need to put in a state on what we can start the hanoi sollution
                pegs.appendleft(pegs.pop())
                if debug:
                    print(f"{moves:0>3} EXTRA  +1 | {previous_state} | {source} -{disc}-> {destination} ({move_smallest_disc}) | {ref_pegs}\r\n       {', '.join(movements)}\r\n")
                    previous_state = repr(ref_pegs)
                moves = 0
            else:
                moves = -1
            extra_moves = 0
            if debug: print(f"Going to the normal solution: {previous_state}\r\n")
        # alter between moves of the lower disc or the other possible movement
        elif move_smallest_disc:
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
            print(f"{moves:0>3} | {previous_state} | {source} -{disc}-> {destination} ({move_smallest_disc}) | {ref_pegs}\r\n       {', '.join(movements)}\r\n")
            sleep(0.2)
        moves += 1

    return movements


rl = sys.stdin.readline
sys.stdin = open("/dev/tty")
boats, trips = map(int, rl().split())  # n, k

a = Tower('A', range(boats, 0, -1))  # Portugal
b = Tower('B')  # China
c = Tower('C')  # England

movements = hanoi_tower_solver(boats, a, c, b, trips)

if debug: print(f"\r\nSolution expected in {trips} and found in {len(movements)} movements:")
print('\n'.join(movements))
