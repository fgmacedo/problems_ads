#!/usr/bin/env python3
"""
Turn the script executable:

> chmod +x ./<name>.py
"""
import sys
from collections import deque

rl = sys.stdin.readline

number_of_inputs = int(rl())
time_transport = 2


class Station:
    def __init__(self, name, cargo_in_b):
        self.name = name
        self.b = deque(cargo_in_b)

    def __len__(self):
        return len(self.b)


for _ in range(number_of_inputs):
    # n - Number of stations (2 <= n <= 100)
    # s - capacity of the cargo carrier (1 <= S <= 100), maximum number carrier can carry.
    # q - maximum number of cargoes the queue in platform B can accommodate (1 <= Q <= 100)
    n, s, q = map(int, rl().split())

    station_count, cargo_max, station_max = n, s, q

    stations = deque(
        Station(idx + 1, map(int, rl().split()[1:])) for idx in range(station_count)
    )

    carrier = deque()
    time_cum = 0
    while True:  # has cargo
        # arrive at nest station
        station = stations[0]

        # attempt to unload cargo
        # for each cargo, if it has the station at target, unloads to A
        #   else, unloads to the end of queue B if has space.
        unload_operations = 0
        while carrier and (
            station_max - len(station.b) > 0 or carrier[-1] == station.name
        ):
            unload_operations += 1
            cargo = carrier.pop()
            if cargo != station.name:
                station.b.append(cargo)

        # then loads cargo from queue B until is empty or carrier is full
        load_operations = min(cargo_max - len(carrier), len(station.b))
        for _ in range(load_operations):
            cargo = station.b.popleft()
            carrier.append(cargo)

        time_cum += unload_operations + load_operations

        if not carrier and not any(stations):
            break

        time_cum += time_transport
        stations.append(stations.popleft())  # rotate stations

    print(f"{time_cum}")
