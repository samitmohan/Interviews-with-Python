# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description/?envType=daily-question&envId=2025-05-07


'''
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
import heapq
class Solution:
    def minTimeToReach(self, moveTime):
        m, n = len(moveTime), len(moveTime[0]) # row, col
        dir = [-1, 0, 1, 0, -1]
        def isValid(row, col, m, n):
            return 0 <= row < m and 0 <= col < n
        minHeap = [(0,0,0)] # (time, row, col)
        vis = [[False] * n for _ in range(m)]
        vis[0][0] = True
        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if r == m-1 and c == n-1: return time # ans
            for i in range(4):
                new_row, new_col = r + dir[i], c + dir[i+1]
                if isValid(new_row, new_col, m, n) and not vis[new_row][new_col]:
                    new_time = 1 + max(time, moveTime[new_row][new_col])
                    heapq.heappush(minHeap, (new_time, new_row, new_col))
                    vis[new_row][new_col] = True
        return -1


# more on dj

class Solution:
    def minTimeToReach(self, moveTime):
        inf = float('inf')
        num_rows, num_cols  = len(moveTime), len(moveTime[0])
        cache = [[inf] * num_cols for _ in range(num_rows)]
        min_heap = []
        heapq.heappush(min_heap, (0, 0, 0)) # timecost, newrow, newcol
        while min_heap:
            cost, row, col = heapq.heappop(min_heap)
            if row == num_rows-1 and col == num_cols-1: # ans found
                continue
            
            for _row, _col in [[-1, 0], [1, 0], [0, 1], [0, -1]]: # new row, new col
                new_row = _row + row
                new_col = _col + col
                if new_row < 0 or new_col < 0 or new_row == num_rows or new_col == num_cols: # boundary check
                    continue
                
                new_cost = max(moveTime[new_row][new_col], cost) + 1
                if new_cost < cache[new_row][new_col]:
                    cache[new_row][new_col] = new_cost # update
                    heapq.heappush(min_heap, (new_cost, new_row, new_col))
        return cache[-1][-1]



s = Solution()
print(s.minTimeToReach(moveTime = [[0,4],[4,4]]))



        