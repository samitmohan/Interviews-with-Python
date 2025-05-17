# https://leetcode.com/problems/insert-interval/
# Time and Space : O(N)


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        ans = []
        for i in range(len(intervals)):
            # edge cases
            if newInterval[1] < intervals[i][0]:  # end val < start val
                ans.append(newInterval)
                return ans + intervals[i:]  # remaining goes after the new internal
            elif newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
            else:
                # overlapping
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
                # this new interval can overlap with other intervals
        ans.append(newInterval)
        return ans
