# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

# Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]

# Simple BFS
"""
Knight has 8 possible moves, for each move check whether knight is still in chess board after moves
    Add next square to the queue if it is still in chess board
Once square [x, y] is reached : return steps to reach square.
"""


class Solution:
    def minKnightMoves(x, y):
        q = deque([0, 0])
        ans = 0
        vis = {(0, 0)}
        directions = ((-2, 1), (-1, 2), (1, 2), (2, 1),
                      (2, -1), (1, -2), (-1, -2), (-2, -1))
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()  # curr possible
                if (i, j) == (x, y):
                    return ans
                for a, b in directions:
                    c, d = i + 1, j + b
                    if (c, d) not in vis:
                        vis.add((c, d))
                        q.append((c, d))  # new squares
            ans += 1
        return -1  # not present
