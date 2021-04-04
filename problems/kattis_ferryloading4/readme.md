# Ferry Loading IV

Problem: https://open.kattis.com/problems/ferryloading4

Before bridges were common, ferries were used to transport cars across rivers. River ferries, unlike their larger cousins, run on a guide line and are powered by the river’s current. Cars drive onto the ferry from one end, the ferry crosses the river, and the cars exit from the other end of the ferry.

There is an l-meter-long ferry that crosses the river. A car may arrive at either river bank to be transported by the ferry to the opposite bank. The ferry travels continuously back and forth between the banks so long as it is carrying a car or there is at least one car waiting at either bank. Whenever the ferry arrives at one of the banks, it unloads its cargo and loads up cars that are waiting to cross as long as they fit on its deck. The cars are loaded in the order of their arrival; ferry’s deck accommodates only one lane of cars. The ferry is initially on the left bank where it broke and it took quite some time to fix it. In the meantime, lines of cars formed on both banks that await to cross the river.

## Input
The first line of input contains an integer 1≤c≤20, the number of test cases. Each test case begins with two integers 1≤l≤500 and 1≤m≤10000. Then follow m lines describing the cars that arrive in this order to be transported. Each line gives the length of a car (an integer number of centimeters between 1 and 100000, inclusive), and the bank at which the car arrives (“left” or “right”).

## Output
For each test case, output one line giving the number of times the ferry has to cross the river in order to serve all waiting cars.

Sample input:

```
4
20 4
380 left
720 left
1340 right
1040 left
15 4
380 left
720 left
1340 right
1040 left
15 4
380 left
720 left
1340 left
1040 left
15 4
380 right
720 right
1340 right
1040 right
```

Sample output:

```
3
3
5
6
```
