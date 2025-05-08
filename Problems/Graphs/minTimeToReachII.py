# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/?envType=daily-question&envId=2025-05-08

#  and two seconds for the next, alternating between the two -> keep parity
from collections import defaultdict
import heapq
class Solution:
    def minTimeToReach(self, moveTime):
        '''
        Djikstra Shortest Path
        '''
        inf = float('inf')
        num_rows, num_cols = len(moveTime), len(moveTime[0])
        visited = [[[False, False] for _ in range(num_cols)] for _ in range(num_rows)]
        mh = []
        heapq.heappush(mh, (0, 0, 0, 0)) # cost, new row, new col, parity


        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while mh:
            cost, row, col, parity = heapq.heappop(mh)
            if visited[row][col][parity]: continue
            visited[row][col][parity] = True

            # else
            # boundary check
            if row == num_rows - 1 and col == num_cols - 1: 
                return cost

            for dr, dc in dirs:
                nextRow = row + dr
                nextCol = col + dc
                if 0 <= nextRow < num_rows and 0 <= nextCol < num_cols:
                    # perform djikstra
                    wait = moveTime[nextRow][nextCol]
                    move_duration = 1 if parity == 0 else 2 # alt moves
                    nextCost = max(wait, cost) + move_duration
                    next_parity = 1 - parity
                    if not visited[nextRow][nextCol][next_parity]:
                        heapq.heappush(mh, (nextCost, nextRow, nextCol, next_parity))
        return -1 # in case no path

s = Solution()
print(s.minTimeToReach(moveTime = [[0,4],[4,4]]))

'''
notes

You're in the top-left room of a grid, and you want to reach the bottom-right room as fast as possible.
But here's the twist:
    Each room has a timer (moveTime[r][c]) that tells you the earliest time you can enter it.
    AND every move you make alternates between taking 1 second, then 2 seconds, then 1, then 2...
        First move: 1 sec
        Second move: 2 sec
        Third move: 1 sec
        Fourth move: 2 sec


while there are still rooms in the heap:
    get the room with the smallest time

    if we already visited this room with this parity, skip

    if we're at the goal (bottom-right), return the time

    for each direction (up/down/left/right):
        check if the next room is inside the grid
        figure out:
            - how long you must wait before it's unlocked (from moveTime)
            - how long this move takes (1 sec if even step, 2 if odd)
            - total time = max(current time, unlock time) + move duration
            - next parity flips (even ↔ odd)

        if we haven't visited next room with that parity:
            push it into the heap
Each room can be visited twice:
    Once when it’s your turn to make a 1-sec move.
    Once when it’s a 2-sec move.

And those two paths may lead to totally different futures.
'''
