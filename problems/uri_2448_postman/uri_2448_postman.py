#!/home/fernando/.pyenv/versions/3.8.1/envs/curso_aed/bin/python
import sys

rl = sys.stdin.readline
rl() # discart n, m info

houses = {x: idx for idx, x in enumerate(rl().split())}
cum_time = 0
current_house_index = 0
for order in rl().split():
    order_house_index = houses[order]
    cum_time = cum_time + abs(order_house_index - current_house_index)
    current_house_index = order_house_index

sys.stdout.write(f"{cum_time}\n")
