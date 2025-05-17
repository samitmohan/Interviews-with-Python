# https://leetcode.com/problems/number-of-islands/
# Simple BFS

from collections import deque


def numIslands(grid):
    if not grid:
        return False
    rows, cols = len(grid), len(grid[0])
    visit = set()  # to store r,c
    islands = 0

    # BFS
    def bfs(r, c):
        q = deque()
        # add starting r, c in visit and queue
        visit.add((r, c))
        q.append((r, c))
        # bfs for neighbouring r, c = r + dr, c + dc
        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # up down left right
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (
                    r in range(rows)
                    and c in range(cols)
                    and grid[r][c] == "1"
                    and (r, c) not in visit
                ):
                    q.append((r, c))
                    visit.add((r, c))

    # ANS
    for r in range(rows):
        for c in range(cols):
            if (
                grid[r][c] == "1" and (r, c) not in visit
            ):  # island and never visited before
                bfs(r, c)
                islands += 1
    return islands


def main():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(numIslands(grid))


main()
