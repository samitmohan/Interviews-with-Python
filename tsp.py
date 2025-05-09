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
probably too many to compute by hand but easy to evaluate with a computer. However, factorials grow very quickly. 
 If you are trying to visit 30 cities, there are 30! different paths. 
This is a huge number. Its about 265 nonillion and has 33 digits. Even for a computer, this is too many paths to examine individually.

Algorithm             | Approach                 | Complexity         |
|-----------------------|--------------------------|--------------------|
| Brute Force           | Exact                    | O(n!)              |
| Dynamic Programming   | Exact                    | O(n^2 * 2^n)       |
| Branch and Bound      | Exact                    | O(n!)              |
| Genetic Algorithms    | Heuristic                | Depends on params  |

The time complexity is determined by the total number of permutations. 
Since the number of permutations is (n-1)! * n, the time complexity of the brute force method to solve the TSP is O((n-1)! * n) which can be simplified to O(n!).
'''


import matplotlib.pyplot as plt
import random
import time

def visualise(cities, path):
    x, y = [cities[i][0] for i in path], [cities[i][1] for i in path]
    plt.figure(figsize=(8, 6))
    for i, (x_coord, y_coord) in enumerate(cities):
        plt.text(x_coord + 0.3, y_coord, f"{city_labels[i]}", fontsize=9)

    plt.plot(x, y, 'o-', color='blue', markersize=10, linewidth=2)
    plt.title("TSP Path Visualization")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

# Brute Force soln -> O(N!) -> generates all possible permutations and calc total dist for each permutation
from itertools import permutations
def tsp_BF(matrix, city_labels, cities, use_custom_perm=False):
    ''' returns shortest distance / min cost to travel all states and come back in factorial time'''
    matrix[0][0] = 0 # start point
    start = 0
    min_cost = float('inf')
    indices = [i for i in range(len(matrix)) if i != start]
    perms = generate_permutations(indices) if use_custom_perm else permutations(indices)

    for i in perms:
        # build  start → permuted cities → back to start
        # also exclude start city from permutations
        path = [start] + list(i) + [start]
        dist = 0
        for j in range(len(path) - 1):
            dist += matrix[path[j]][path[j+1]] # adj paths

        if dist < min_cost:
            min_cost = dist
            best_path = path
    best_path_labels = [city_labels[i] for i in best_path]
    # visualise(cities, best_path)
    return min_cost, best_path_labels

# itertools.permutations
def generate_permutations(arr):
    if len(arr) == 0: return [[]]
    perms = []
    for i in range(len(arr)):
        curr = arr[i]
        rest = arr[:i] + arr[i+1:]
        for p in generate_permutations(rest):
            perms.append([curr] + p)
    return perms

def main():
    # graph[i][j] is the distance from city i to city j
            # Delhi Bombay Bihar Bangalore
    #Delhi  [                             ]
    #Bombay [                             ]
    #Bihar  [                             ]
    #Bangalore [                          ]
    graph = [
            [0, 1162, 908, 1744], 
            [1153, 0, 840, 845], 
            [894, 1445, 0, 1568], 
            [1744, 845, 1630, 0] 
            ]


    cities = [
        (0, 0),  # Delhi
        (1162, 0),  # Bombay
        (894, 800),  # Bihar
        (1744, 500)  # Bangalore
    ]
    city_labels = ["Delhi", "Bombay", "Bihar", "Bangalore"]

    # True = Custom Perm (19 microsec) | False = Itertools (10 microsec)
    use_custom_perm = False

    method = "Custom Permutations" if use_custom_perm else "itertools.permutations"
    print(f"Using: {method}")
    start_time = time.perf_counter()
    min_cost, best_path = tsp_BF(graph, city_labels, cities, use_custom_perm=use_custom_perm)
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000000
    print(f"Execution Time: {execution_time_ms:.4f} microseconds")

    print(f"Minimum distance from start vertex to visit all cities and come back: {min_cost}")
    print(f"Best path: {best_path}")

main()


# DP Solution