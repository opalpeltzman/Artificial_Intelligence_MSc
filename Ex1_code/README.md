# Heuristic Search

## MyWay

MyWay is a road search program that works with data file `israel.csv` downloaded from `www.openstreetmap` that represents Israel road map.

In this program I implemented *UCS*, *A** and *IDA** search algorithms in order to solve 100 random search problems I generated from the given road map.
___
Each algorithm, mentioned above, goal is to find the best way from start point to destination. The best way
is defined by the road distance in KM and the road speed range. 
___

How to Use?
```python
python main.py [algorithm] [start point] [destination]
```
algorithms-
1. ucs
2. astar

**[start, destination]** example-
- 30 55

all possible **[start, destination]** points foe each algorithm are available at `results`
___		
results/
Experiment results for *UCS* and *A** algorithms represents-
- The route
- The time it took to complete the route
- Estimated time
