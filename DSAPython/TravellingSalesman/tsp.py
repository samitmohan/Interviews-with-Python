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

Cities	Use Brute Force?	Use Held-Karp (DP)?
≤ 8	    ✅ Yes	           ✅ Optional
9–16	❌ No	           ✅ Yes
> 20	❌ No	           ⚠ Too slow (use heuristics like Genetic/ACO)
'''


import matplotlib.pyplot as plt
import random
import time

def visualise(cities, path, city_labels):
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




# DP Solution
'''
we build optimal paths from smaller subsets using memoization.
for n cities we have 2^n possible subsets
each subset can be represented using bitmask

Subset(Cities Visited)  | Bitmask	| Decimal
{}	                    |   0000	|    0
{0}	                    |   0001    |    1
{0, 1}	                |   0011	|    3
{0, 2, 3}	            |  1101	    |   13
{0, 1, 2, 3}	        |  1111	    |   15

Each bit is 1 if city is visited 0 else

Min cost to reach city i having visited cities in mask (subsets) and ending at i
mask = 0 to 2^n-1 {all subsets}
i = 0 to n-1 {last visited city}

Time complexity -> O(n × 2**n)

start at city 0

dp[mask][i] means min cost to reach city i after travelling to mask cities (mask includes city i and 0 and we end at city i)

left shift << multiplying number by 2
start at city 0 -> go directly to some city i ≠ 0

https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm

function algorithm TSP (G, n) is
    for k := 2 to n do ~~~ FROM k = 2 to len of matrix
        g({k}, k) := d(1, k) ~~~~ find ways to travel from 1 to k
    end for

    for s := 2 to n−1 do ~~~ for all subsets
        for all S ⊆ {2, ..., n}, |S| = s do 
            for all k ∈ S do
                g(S, k) := minm≠k,m∈S [g(S\{k}, m) + d(m, k)] ~~~ find the min path out of all subsets of g(S, k)
            end for
        end for
    end for

    opt := mink≠1 [g({2, 3, ..., n}, k) + d(k, 1)]
    return (opt)
end function

'''

def tsp_DP(graph, city_labels, cities):
    '''Dynamic Programming + Bitmasking approach to solve TSP in O(n^2 * 2^n)'''
    n = len(graph)
    ALL_VISITED = (1 << n) - 1
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]

    dp[1][0] = 0  # Start at city 0 with only city 0 visited

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)): continue
            for v in range(n):
                if (mask & (1 << v)) == 0:
                    new_mask = mask | (1 << v)
                    new_cost = dp[mask][u] + graph[u][v]
                    if new_cost < dp[new_mask][v]:
                        dp[new_mask][v] = new_cost
                        parent[new_mask][v] = u

    # minimum cost to return to starting city (0)
    min_cost = float('inf')
    last_city = -1
    for i in range(1, n):
        cost = dp[ALL_VISITED][i] + graph[i][0]
        if cost < min_cost:
            min_cost = cost
            last_city = i

    path = []
    mask = ALL_VISITED
    curr = last_city
    while curr != -1:
        path.append(curr)
        next_curr = parent[mask][curr]
        mask = mask ^ (1 << curr)
        curr = next_curr
    path.append(0)
    path.reverse()

    best_path_labels = [city_labels[i] for i in path]
    # visualise(cities, path)
    return min_cost, best_path_labels



# Nearest Neighbor Algorithm


def main():
    # BF
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
    use_custom_perm = True

    method = "Custom Permutations" if use_custom_perm else "itertools.permutations"
    print(f"\n Brute Force Method ({method})")
    print(f"Using: {method}")
    start_time = time.perf_counter()
    min_cost, best_path = tsp_BF(graph, city_labels, cities, use_custom_perm=use_custom_perm)
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000000
    print(f"Execution Time: {execution_time_ms:.4f} microseconds")

    print(f"Minimum distance from start vertex to visit all cities and come back: {min_cost}")
    print(f"Best path: {best_path}")


    # ---------- Dynamic Programming ----------
    print(f"\n Dynamic Programming (Held-Karp)")
    start_time = time.perf_counter()
    min_cost_dp, best_path_dp = tsp_DP(graph, city_labels, cities)
    end_time = time.perf_counter()
    execution_time_dp = (end_time - start_time) * 1000000
    print(f"Execution Time: {execution_time_dp:.4f} µs")
    print(f"Minimum distance: {min_cost_dp}")
    print(f"Best path: {best_path_dp}")
    # visualise(cities, [city_labels.index(name) for name in best_path_dp], city_labels)


main()

# https://medium.com/basecs/speeding-up-the-traveling-salesman-using-dynamic-programming-b76d7552e8dd