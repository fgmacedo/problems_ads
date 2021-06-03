#!/usr/bin/env python3
"""
Turn the script executable:

> chmod +x ./<name>.py

Example input:

    3
    5 2
    6 3
    1234 233

Expected output:

    Case 1: 3
    Case 2: 1
    Case 3: 25
"""
import sys

rl = sys.stdin.readline
number_of_testcases = int(rl())


class NoEnc:
    def __init__(self, v, ant=None, prox=None):
        self.v = v
        self.ant = ant
        self.prox = prox

    def remove(self):
        self.ant.prox = self.prox
        self.prox.ant = self.ant
        return self


class LoopList:
    def __init__(self, no, step=1):
        self.no = no
        self.step = step

    def __iter__(self):
        self.no = self.no.ant
        self.visited_same_node = 0
        return self

    def __next__(self):
        for _ in range(self.step):
            if self.no == self.no.prox:
                self.visited_same_node += 1
                if self.visited_same_node > self.step:
                    raise StopIteration
            self.no = self.no.prox
        return self.no


class ListaEnc:
    def __init__(self, cur=None):
        self.cur = cur

    def add(self, v):
        no = NoEnc(v)
        if self.cur is None:
            self.cur = no
            self.cur.prox = no
            self.cur.ant = no
        else:
            ant = self.cur.ant
            no.prox = self.cur
            no.ant = ant
            self.cur.ant = no
            if ant:
                ant.prox = no
        return no

    def loop(self, step=1):
        return LoopList(self.cur, step)


results = []
for case_no in range(1, number_of_testcases + 1):
    # n (1 ≤ n ≤ 10000 ): peoples in the circle
    # k (1 ≤ k ≤ 1000): jump step to the next man that will be killed
    n, k = map(int, rl().split())

    l = ListaEnc()
    for i in range(1, n + 1):
        l.add(i)

    gen = l.loop(k)

    for item in gen:
        item.remove()

    results.append(f"Case {case_no}: {item.v}")

if results:
    sys.stdout.write("\n".join(results) + "\n")
