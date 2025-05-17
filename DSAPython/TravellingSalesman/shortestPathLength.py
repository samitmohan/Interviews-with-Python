# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# (current_node = i, visited_mask = (1 << i), distance = 0

"""
Explanation of the Python Code:

    n = len(graph): Gets the number of nodes.
    Edge Cases (n == 0 or n == 1):
        If there are no nodes, the path length is 0 (or arguably undefined, but LeetCode tests might expect 0).
        If there's only one node, we've already "visited" it, so the path length is 0.
    target_mask = (1 << n) - 1:
        This creates a bitmask where all n bits are set to 1.
        1 << n creates a number like 100...0 (1 followed by n zeros).
        Subtracting 1 gives 11...1 (n ones).
    queue = collections.deque(): Initializes a double-ended queue, which is efficient for BFS (popping from the left).
    visited = set(): Initializes a set to store tuples of (node, mask) that have already been added to the queue. This prevents reprocessing the same state, which is crucial for efficiency and correctness (avoiding infinite loops in graphs with cycles).
    Initialization Loop (for i in range(n):):
        We can start from any node. So, for each node i, we add an initial state to the queue.
        initial_mask = (1 << i): The mask representing that only node i has been visited.
        queue.append((i, initial_mask, 0)): Add the starting node, its mask, and distance 0 to the queue.
        visited.add((i, initial_mask)): Mark this initial state as visited.
    BFS Loop (while queue:):
        curr_node, mask, dist = queue.popleft(): Get the current state from the front of the queue.
        Check for Target: if mask == target_mask: return dist
            If the current mask equals target_mask, it means all nodes have been visited. Since BFS explores layer by layer, this is guaranteed to be the shortest path to achieve this state. We return the current dist.
        Explore Neighbors (for neighbor in graph[curr_node]:):
            new_mask = mask | (1 << neighbor): Create the new mask by performing a bitwise OR with (1 << neighbor). This sets the bit corresponding to the neighbor node, indicating it has now been visited in this path.
            if (neighbor, new_mask) not in visited::
                This is the crucial check. If we haven't encountered this specific combination of neighbor node and new_mask before, it's a new state worth exploring.
                visited.add((neighbor, new_mask)): Mark it as visited.
                queue.append((neighbor, new_mask, dist + 1)): Add the new state (the neighbor, the updated mask, and the incremented distance) to the queue.
    return -1 (Fallback): The problem guarantees the graph is connected, meaning a path visiting all nodes always exists. So, this line should ideally not be reached.

This approach systematically explores all possible paths, leveraging BFS to find the shortest one, while using bitmasks to efficiently track the set of visited nodes in each path.

"""

from collections import deque


def shortestPathLength(graph):
    n = len(graph)
    if n == 0:
        return 0
    if n == 1:
        return 0  # path len is 0 if only one node
    # target mask is when all bits are set to 1 -> 111
    targetMask = (1 << n) - 1
    q = deque()
    vis = set()
    """
    Initialise q -> for each starting node i
        initial mask has only ith bit set
        initial dist = 0
    """
    for i in range(n):
        initMask = 1 << i
        q.append((i, initMask, 0))
        vis.add((i, initMask))
    while q:
        currNode, mask, dist = q.popleft()
        if mask == targetMask:
            return dist  # visited all
        # explore neigh
        for neigh in graph[currNode]:
            newMask = mask | (1 << neigh)
            if (neigh, newMask) not in vis:
                vis.add((neigh, newMask))
                q.append((neigh, newMask, dist + 1))
    return -1


def main():
    print(shortestPathLength(graph=[[1, 2, 3], [0], [0], [0]]))  # 4


main()
