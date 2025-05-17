# https://leetcode.com/problems/minimum-size-subarray-sum/description/
# Dynamic Sized SW
# Find SW with target and then contract the window until min found
# two pointers : shift
# while our window is valid keep incrementing the left pointer (shrink window size)
# once invalid : shift right pointer until it's out of bounds
# keep track of min_length and update it as well as the currsum (total)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        total = 0
        ans = float("inf")  # if we dont find an array then return 0

        for right in range(len(nums)):
            total += nums[right]
            while (
                total >= target
            ):  # answer found :: get size of window : (right - left + 1)
                ans = min(right - left + 1, ans)
                # increment left pointer to find smaller window and also subtract deleted left pointer from total
                total -= nums[left]
                left += 1

        return 0 if ans == float("inf") else ans
