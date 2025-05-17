# https://leetcode.com/problems/non-overlapping-intervals/
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort
        intervals.sort()
        ans = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                ans += 1
                prev_end = min(end, prev_end)
        return ans
