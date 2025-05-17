# https://leetcode.com/problems/merge-intervals/
# Sort by start value
# O(n(log(n)) : Sort


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])  # sort by start val
        ans = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = ans[-1][1]  # end val of most recently added element
            if start <= last_end:  # overlap
                ans[-1][1] = max(last_end, end)
            else:
                ans.append([start, end])
        return ans
