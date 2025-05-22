# https://leetcode.com/problems/zero-array-transformation-iii/description/?envType=daily-question&envId=2025-05-22
"""
Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]
Output: 1
Explanation:
After removing queries[2], nums can still be converted to a zero array.
    Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
    Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.


States: used, valid, seen (but not used), invalid
1) Push all queries starting at ith index to available queries pool
2) Reuse if any query was already included & still valid
3) If more query is required, get them from available queries pool and push to used queries pool
4) If insufficient queries, return -1
else
    remove queries ending at ith index from used queries pool
repeat

Take advantage of overlapping queries (prefer bigger queries) & also sort queries by start index (intuitive)
    We need queries with highest end index to be used first

Greedily use the biggest queries first
    used pool is sorted by end index (minheap)
    available pool is sorted by start index (maxheap)

Queries transferred from available to used pool = t, answer = total_queries - t {these many queries are not used}
Time Complexity: O(Q.logQ {sorting} + N.logQ {iterate per posn, heap push pop})
Space Complexity: O(Q)
"""

from typing import List
import heapq


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        used_query = []  # stores end points
        available_query = []  # stores start points (end points using neg val)
        queries.sort(key=lambda x: x[0])  # sort by start posn

        # process all points
        query_posn = 0
        used_count = 0

        for i in range(n):
            # push all queries starting at 'i' into available query (max heap)
            while query_posn < len(queries) and queries[query_posn][0] == i:
                end = queries[query_posn][1]
                heapq.heappush(available_query, -end)
                query_posn += 1

            # adjust nums[i] by subtracting number of active queries covering/overlapping it
            nums[i] -= len(used_query)

            # apply queries if nums[i] > 0
            while nums[i] > 0 and available_query and -available_query[0] >= i:
                end = -heapq.heappop(available_query)
                heapq.heappush(used_query, end)
                nums[i] -= 1
                used_count += 1

            # can't manage enough queries (nums[i] can't be reduced to 0)
            if nums[i] > 0:
                return -1

            # remove all queries used and ending at i
            while used_query and used_query[0] == i:
                heapq.heappop(used_query)

        # number of unused queries = ans
        return len(queries) - used_count


sol = Solution()
print(sol.maxRemoval([2, 0, 2], [[0, 2], [0, 2], [1, 1]]))  # Output: 1
