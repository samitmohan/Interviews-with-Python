# Both Problems
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description/?envType=daily-question&envId=2025-05-07
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/?envType=daily-question&envId=2025-05-08

#  and two seconds for the next, alternating between the two -> keep parity
from collections import defaultdict
import heapq
# bfs + min_heap
'''
moveTime = [[0,4],[4,4]]
Output 5 Expected 6
'''
from heapq import heappush, heappop
def minTimeToReach(moveTime):
    num_rows = len(moveTime)
    num_cols = len(moveTime[0])
    dirns = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    inf = float('inf')
    cache = [[inf] * num_cols for _ in range(num_rows)] # answer array
    cache[0][0] = 0
    heap = []
    heappush(heap, (0, 0, 0)) # current_time, row, col
    while heap:
        currTime, row, col = heappop(heap) # get the current cost row col
        # now need to check boundaries
        if row == num_rows - 1 and col == num_cols - 1: return currTime
        if currTime > cache[row][col]: continue

        for dr, dc in dirns:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                next_time = max(currTime, moveTime[new_row][new_col]) + 1
                if next_time < cache[new_row][new_col]:
                    cache[new_row][new_col] = next_time
                    heappush(heap, (next_time, new_row, new_col))
    return -1
        

'''
Now for next problem -> Can move 1 step or 2 step dependening on parity.
move 1 = 1 
move 2 = 2
move 3 = 1
# need to add parity bit in heap
move_duration = 1 if parity % 2 != 0 else 2
'''

def minTimeToReach2(moveTime):
    nr, nc = len(moveTime), len(moveTime[0])
    dirns = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    inf = float('inf')
    cache = [[inf] * nc for _ in range(nr)] # answer array
    cache[0][0] = 0
    mh = []
    heappush(mh, (0, 0, 0, 0)) # currtime, row, col, parity
    while mh:
        currTime, row, col, parity = heappop(mh)
        if row == nr - 1 and col == nc - 1: return currTime
        if currTime > cache[row][col]: continue
        for dr, dc in dirns:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < nr and 0 <= new_col < nc: # in boundary
                moveDuration = 1 if parity == 0 else 2
                nextTime = max(currTime, moveTime[new_row][new_col]) + moveDuration
                if nextTime < cache[new_row][new_col]:
                    cache[new_row][new_col] = nextTime # djkstra
                    new_parity = 1 - parity 
                    heappush(mh, (nextTime, new_row, new_col, new_parity))
    return -1



def main():
    print(minTimeToReach(moveTime=[[0,4],[4,4]])) # 6
    print(minTimeToReach2( moveTime = [[0,4],[4,4]])) # 7
main()

            
        


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

takes one second to move
if curr_time >= next destination time -> simply add 1 to timer and jump to next destination
if not then add next_destination_time to current timer = t += next_dest_time + 1
BFS is used when all costs are same -> in this they arent. -> So need to apply Djikstra -> BFS + Heap (Greedy)

For any cell you have 4 adjacent cells = (i+1, j) (i-1, j) (i, j+1) and (i, j-1) from (i,j) + check for bounds (only for valid indices)

node(int row, col, time, cost)
time = min(curr.time, moveTime[new_row][new_col]) + 1
visited array= false
minheap = (0,0,0) {row, col, time}
curr time = max(curr_time, nextlocation) + 1
TC : O((nm)lognm) nm due to min heap

'''
