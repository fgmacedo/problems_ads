
# The Lonesome Cargo Distributor

The Plussians believe that the Airport Based Cargo Distribution & Embarkation Facility (ABCDEF in
short) at the Cosco International Airport (CIA) is the largest such facility in the whole world though
second largest in Plussia. Cargo planes arrive from and leave for many countries all around the world
(Cermany, Q.S.A, Capan, Custralia etc. are some to name). ABCDEF is engaged in distributing,
loading and unloading the cargoes carried by these planes.

Each cargo is a cubic box of fixed size and has a tag attached to it naming the destination country.
For convenience, each country is assigned a unique ID. For example, if there are n countries, each
country gets a unique integer ID ranging from 1 to n.

Every country X has its own cargo station identified by its country ID. There are two platforms
(platform A and platform B) in each station. In platform A are put those cargoes which are to be
transported (by air) to country X at some convenient time. Platform B is actually a queue of cargoes
which are to be carried to countries other than country X. The cargo stations have a circular (ring)
arrangement, that is, if there are n stations then each of the following station-pairs are adjacent:
(1, 2),(2, 3),(3, 4), . . . ,(n − 1, n) and (n, 1).

ABCDEF has many land-based cargo carriers used to carry cargo from station to station. But these
carriers have so narrow space that you cannot even put two cargoes side by side. A carrier can carry
more than one cargo (although there is a limit on the maximum number of cargoes a carrier can carry)
only by putting them (the cargoes) on top of one another. This stack arrangement has the problem
that you cannot just remove any cargo from the stack as you wish. For example, to remove the 3rd
cargo from the top you must first remove the topmost two cargoes.

A cargo carrier moves from station to station strictly following their ring arrangement, that is, from
station 1 it moves to station 2, then to 3, then 4, ..., then n, then 1 again, etc.. It requires exactly 2
minutes to move from any station to its adjacent one.

After reaching any station (say, station X), the cargo carrier first attempts to unload cargo. Starting
from the topmost cargo in its stack, it checks the tag attached to the cargo. If it finds that the cargo
has destination X, then it unloads it (the cargo) to platform A, otherwise it checks to see whether
the queue in platform B has any vacant position, and if so it puts the cargo at the rear of the queue.
This unloading procedure continues from the top to the bottom of the stack until one fails or the stack
becomes empty, whichever comes first. Each successful unloading attempt requires exactly 1 minute,
that is, unloading 3 cargoes in a station will require exactly 3 minutes. After unloading is complete,
the carrier begins to load. The carrier continues to take the cargo in front of the queue in platform B
and put it on top of its stack until the queue is empty or the stack is full, whichever comes first. Each
successful loading attempt also requires exactly 1 minute, that is, loading 4 cargoes from a station will
require exactly 4 minutes. After loading is complete, the carrier moves to the next station in the ring.
In this way, for many years, the cargo carriers are doing the job of moving the cargoes from platform
B to platform A of appropriate stations from where the cargo planes carry them (the cargoes) to their
destination countries.

But, after a conflict with the management regarding the pay scale, the employees of ABCDEF have
gone to a strike for indefinite period from the last Sunday. Planes are arriving and leaving, but no
one is there to load and unload the cargo. There is no one to distribute the queued cargoes to their
destination stations. The entire facility has now come to a standstill.
But, you, as always known to and hated by your colleagues as the boss’s man, have decided to
break the strike and save CIA. You are going to start working from tomorrow morning and distribute
the queued cargoes to their appropriate stations using a cargo carrier. Initially your carrier will be
empty and, you will start your journey from station 1 and continue to move around the ring until all
the cargoes have been distributed to their destination stations. But before starting the job, you have
decided to write a program to determine exactly how long it will take to complete it.

### Input

The input contains several sets of input. The first line of the input file contains an integer SET, which
indicates how many sets of inputs are there. It is then followed by SET sets of inputs. In our sample
input the value of SET is 2.
The first line of the input contains three integers: N, S and Q. N (2 ≤ N ≤ 100) is the number
of stations in the ring. S (1 ≤ S ≤ 100) is the capacity of your cargo carrier, that is, the maximum
number of cargoes your carrier can carry. Q (1 ≤ Q ≤ 100) is the maximum number of cargoes the
queue in platform B can accommodate. All the queues in the system are assumed to have the same
capacity.
Then follow N lines. Assuming that these lines are numbered from 1 to N, for 1 ≤ i ≤ N, line i
contains an integer Qi (0 ≤ Qi ≤ Q) giving the number of cargoes queued at station i followed by Qi
integers giving the destination stations of the queued cargoes from front to rear. You may assume that
none of these Qi cargoes will have station i as their destination.

### Output
For each set of input output the number of minutes it will take to finish the job in a separate line.


### Sample Input

```
2
5 2 3
3 4 5 2
2 1 3
0
3 3 5 1
1 4
5 2 3
3 4 5 2
2 1 3
0
3 3 5 1
1 4
```

### Sample Output

```
72
72
```
