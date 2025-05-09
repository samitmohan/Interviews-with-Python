'''
Travelling Salesman
Given a list of cities and the distances between each pair of cities, 
What is the shortest possible route that visits each city exactly once and returns to the origin city?

Difficult to solve, easy to verify which makes it NP Hard

Distance calculated is by euclidean distance

Find the shortest possible route that:
    Visits each city exactly once.
    Returns to the starting city.

 However, for n different cities, there are n! different possible paths.

If you only want to visit 5 cities there are 120 different possible paths between them
 – probably too many to compute by hand but easy to evaluate with a computer. However, factorials grow very quickly. 
 If you are trying to visit 30 cities, there are 30! different paths. 
This is a huge number. It’s about 265 nonillion and has 33 digits. Even for a computer, this is too many paths to examine individually.
'''

def tsp_BF(distance):
    ''' returns shortest distance / min cost to travel all states and come back in factorial time'''
    pass

def main():
    distance = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0] ]
    tsp_BF(distance)
main()