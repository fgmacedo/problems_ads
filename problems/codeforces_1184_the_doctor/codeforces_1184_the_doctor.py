#!/usr/bin/env python3
import sys


def selection(l):
    """
    Not the best choice, but easy to implement to not rely on using the built-in sort functions.
    """
    for i in range(len(l) - 1):
        lowest = i
        for j in range(i + 1, len(l)):
            if l[j] < l[lowest]:
                lowest = j
        l[i], l[lowest] = l[lowest], l[i]


def main(rl):
    _s_num_spaceships, b_num_bases = [int(x) for x in rl().split()]
    a_attacking_power = [int(x) for x in rl().split()]

    bases = []
    for _ in range(b_num_bases):
        defensive_power, gold = [int(x) for x in rl().split()]
        bases.append((defensive_power, gold))

    # A simple `bases.sort()` does the job... but it's an ADS class, right?
    # bases.sort()
    selection(bases)

    solutions = []
    for spaceship in a_attacking_power:
        gold = 0
        for p, g in bases:
            if spaceship < p:
                break
            gold += g
        solutions.append(gold)

    return solutions


if __name__ == "__main__":
    rl = sys.stdin.readline
    solution = main(rl)
    print(" ".join(str(x) for x in solution))
