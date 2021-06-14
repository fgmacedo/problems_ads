#!/usr/bin/env python3
import sys
from collections import deque


def main(rl):
    solutions = []
    while True:
        case_solutions = []
        n_number_coachs = int(rl())
        if not n_number_coachs:
            break

        coachs_sample = deque(range(n_number_coachs, 0, -1))

        while True:
            line = rl().split()
            if len(line) == 1:
                break
            query = deque(int(x) for x in line)

            arriving = coachs_sample.copy()
            station, destiny = deque(), deque()

            while query:
                next_requested_coach = query.popleft()
                if not arriving and not station:
                    break

                if (
                    arriving
                    and arriving[-1] > next_requested_coach
                    and station
                    and station[-1] > next_requested_coach
                ):
                    break

                while arriving and arriving[-1] <= next_requested_coach:
                    current_coach = arriving[-1]

                    # if the requested coach is arriving them pass thru the station
                    if current_coach == next_requested_coach:
                        destiny.append(arriving.pop())
                        break
                    elif current_coach < next_requested_coach:
                        station.append(arriving.pop())

                if station and station[-1] == next_requested_coach:
                    destiny.append(station.pop())
                    continue

            solution_found = bool(line == [str(x) for x in destiny])
            solution = "Yes" if solution_found else "No"
            case_solutions.append(solution)

        solutions.append("\n".join(case_solutions))

    return solutions


if __name__ == "__main__":
    rl = sys.stdin.readline
    solutions = main(rl)
    print("\n\n".join(solutions) + "\n")
