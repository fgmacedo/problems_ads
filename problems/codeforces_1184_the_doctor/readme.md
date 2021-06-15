# B1. The Doctor Meets Vader (Easy)

https://codeforces.com/problemset/problem/1184/B1




Heidi and Doctor Who hopped out of the TARDIS and found themselves at EPFL in 2018. They were surrounded by stormtroopers and Darth Vader was approaching. Miraculously, they managed to escape to a nearby rebel base but the Doctor was very confused. Heidi reminded him that last year's HC2 theme was Star Wars. Now he understood, and he's ready to face the evils of the Empire!

The rebels have s spaceships, each with a certain attacking power a.

They want to send their spaceships to destroy the empire bases and steal enough gold and supplies in order to keep the rebellion alive.

The empire has b bases, each with a certain defensive power d, and a certain amount of gold g.

A spaceship can attack all the bases which have a defensive power less than or equal to its attacking power.

If a spaceship attacks a base, it steals all the gold in that base.

The rebels are still undecided which spaceship to send out first, so they asked for the Doctor's help. They would like to know, for each spaceship, the maximum amount of gold it can steal.

## Input
The first line contains integers s and b (1≤s,b≤105), the number of spaceships and the number of bases, respectively.

The second line contains s integers a (0≤a≤109), the attacking power of each spaceship.

The next b lines contain integers d,g (0≤d≤109, 0≤g≤104), the defensive power and the gold of each base, respectively.

## Output
Print s integers, the maximum amount of gold each spaceship can steal, in the same order as the spaceships are given in the input.

## Example
input:
```
5 4
1 3 5 2 4
0 1
4 2
2 8
9 4
```

output:
```
1 9 11 9 11
```
