# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/
"""
Looking for minimum edge basically.
DFS : O(n) / E + V
Hashset so we don't visit the same
"""


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)  # node -> list of (neighbor, distance)
        for src, dst, dist in roads:
            adj[src].append((dst, dist))
            adj[src].append((src, dist))  # bi-directional

        def dfs(i):
            # base case
            if i in visit:
                return
            visit.add(i)
            nonlocal ans
            for n, dist in adj[i]:
                # maybe this dist is min
                ans = min(ans, dist)
                dfs(n)

        ans = float("inf")  # init
        visit = set()
        dfs(1)  # doesn't matter where we start
        return ans
