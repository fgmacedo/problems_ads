#!/usr/bin/env python3
"""
Turn the script executable:

> chmod +x ./<name>.py
"""
import sys
from collections import deque

rl = sys.stdin.readline
debug = "--debug" in sys.argv

number_of_inputs = int(rl())

time_load = 1
time_transport = 2


class Station:
    def __init__(self, name, capacity, cargo_in_b):
        self.name = name
        self.capacity = capacity
        self.b = deque(cargo_in_b)

    @property
    def empty_space(self):
        return self.capacity - len(self)

    def __len__(self):
        return len(self.b)

    def __repr__(self):
        return f"S{self.name}^{len(self.b)}({' '.join(str(x) for x in self.b)})"


for _ in range(number_of_inputs):
    # n - Number of stations (2 <= n <= 100)
    # s - capacity of the cargo carrier (1 <= S <= 100), maximum number carrier can carry.
    # q - maximum number of cargoes the queue in platform B can accommodate (1 <= Q <= 100)
    n, s, q = map(int, rl().split())

    station_count, cargo_max, station_max = n, s, q

    stations = deque(
        Station(idx + 1, station_max, map(int, rl().split()[1:]))
        for idx in range(station_count)
    )
    if debug:
        print(f"\r\n{'*'*40}")
        print(f"station_count:{station_count}")
        print(f"cargo_max:{cargo_max}")
        print(f"station_max:{station_max}")

    carrier = deque()
    time_cum = 0
    iteration = 0

    if debug:
        ref_stations = list(stations)

    while True:  # has cargo
        # arrive at nest station
        station = stations[0]
        if debug:
            print(
                f"I:{iteration:0>3} T:{time_cum:0>4} | {' | '.join(str(x) for x in ref_stations)}\n  C{list(carrier)} at {station}"
            )

        # attempt to unload cargo
        # for each cargo, if it has the station at target, unloads to A
        #   else, unloads to the end of queue B if has space.
        unload_operations = 0
        while carrier and (station.empty_space or carrier[-1] == station.name):
            unload_operations += 1
            cargo = carrier.pop()
            if cargo != station.name:
                station.b.append(cargo)
                if debug:
                    print(f"    📦 {cargo} unloaded into S{station.name}.B")
            elif debug:
                print(f"    📦 {cargo} unloaded into S{station.name}.A (destiny reached)")

        # then loads cargo from queue B until is empty of carrier is full
        load_operations = min(len(station), cargo_max - len(carrier))
        for _ in range(load_operations):
            cargo = station.b.popleft()
            if debug:
                print(f"    📦 {cargo} loaded from S{station.name}.B")
            carrier.append(cargo)

        operations = unload_operations + load_operations
        time_cum += operations
        if debug:
            print(f"  C{list(carrier)} operations: {operations} T:{time_cum:0>4}")

        if not carrier and not any(stations):
            break

        time_cum += time_transport
        stations.append(stations.popleft())  # rotate stations
        if debug:
            print(f"  🚚 moving to next station T:{time_cum:0>4}")
        iteration += 1

    print(f"{time_cum}")
