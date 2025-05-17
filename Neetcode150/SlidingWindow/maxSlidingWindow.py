# https://leetcode.com/problems/sliding-window-maximum/
"""
Draw to get a better picture :
Use a deque : why? -> add and remove last element in O(1) and also remove first element in O(1)
  Monotonic Decreasing Queue : Elements can only be greater than prevs number
Insert elements into DQ until window size reached -> max element will be left most of DQ : q[0] -> append to answer
  increment right += 1 for next window, check for next window :: before checking make sure you remove the out of window value (prevs highest val) from DQ by pop so that you are looking at the right window.
  increment left pointer only when window size is reached
Edge case : can only append to answer if (right + 1) >= k [window is atleast size k]

---DRY RUN---
nums = [8,7,6,9], k = 2
  DQ = [8] {can add because its largest}
  DQ = [8,7] {can add because 8 > 7}
    max size of window reached -> ans.append(dq[0]) : ans array = [8]
  right += 1 and remove out of bound element
  window = [8,7,6] : q[0].popleft() : [7,6]
  DQ = [7,6] {can add because 7 > 6}
    max size of window reached -> ans.append(dq[0]) : ans array = [8,7]
  right += 1 and remove out of bound elementA
  window = [7,6,9] : q[0].popleft() : [6,9]
  DQ = [6] {can't add 9 because 6 !> 9} :: pop from dq and add 9
  DQ = [9] : ans.append(dq[0]) : ans array = [8,7,9]
"""

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        left = right = 0
        while right < len(nums):  # while it doesn't reach the end
            # smaller value exists in q : pop
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)  # otherwise add
            # remove val if out of bounds
            if left > q[0]:
                q.popleft()

            # edge case : can only append to answer if window is of size k
            if (right + 1) >= k:
                ans.append(nums[q[0]])
                left += 1
            right += 1  # else increment right
        return ans
