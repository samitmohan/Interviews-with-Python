import time
import random
import matplotlib.pyplot as plt
from itertools import permutations


# Generate a random complete graph with n cities
def generate_random_graph(n, seed=42):
    random.seed(seed)
    return [
        [0 if i == j else random.randint(100, 1000) for j in range(n)] for i in range(n)
    ]


def tsp_brute_force(graph):
    n = len(graph)
    min_cost = float("inf")
    best_path = []
    for perm in permutations(range(1, n)):
        path = [0] + list(perm) + [0]
        cost = sum(graph[path[i]][path[i + 1]] for i in range(n))
        if cost < min_cost:
            min_cost = cost
            best_path = path
    return min_cost, best_path


def tsp_dp(graph):
    n = len(graph)
    dp = {}

    def visit(mask, pos):
        if mask == (1 << n) - 1:
            return graph[pos][0]
        if (mask, pos) in dp:
            return dp[(mask, pos)]
        min_cost = float("inf")
        for city in range(n):
            if not (mask & (1 << city)):
                new_cost = graph[pos][city] + visit(mask | (1 << city), city)
                min_cost = min(min_cost, new_cost)
        dp[(mask, pos)] = min_cost
        return min_cost

    return visit(1, 0), []


def benchmark(max_cities=10):
    brute_times = []
    dp_times = []
    sizes = list(range(3, max_cities + 1))

    for n in sizes:
        graph = generate_random_graph(n)

        if n <= 8:  # Limit to safe n for brute force
            start = time.perf_counter()
            tsp_brute_force(graph)
            end = time.perf_counter()
            brute_times.append((end - start) * 1000)
        else:
            brute_times.append(None)

        # DP
        start = time.perf_counter()
        tsp_dp(graph)
        end = time.perf_counter()
        dp_times.append((end - start) * 1000)

    return sizes, brute_times, dp_times


sizes, brute_times, dp_times = benchmark(12)

plt.figure(figsize=(10, 6))
plt.plot(sizes, dp_times, "o-", label="DP (Held-Karp)", color="blue")
plt.plot(sizes[: len(brute_times)], brute_times, "o-", label="Brute Force", color="red")
plt.xlabel("Number of Cities")
plt.ylabel("Execution Time (ms)")
plt.title("TSP: Brute Force vs Dynamic Programming")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
