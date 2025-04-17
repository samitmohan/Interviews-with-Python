# https://leetcode.com/problems/count-the-number-of-good-subarrays/?envType=daily-question&envId=2025-04-16
# Window size : r + l - 1
# Always right += 1 and left += 1 when window size reached
# Count number of equal pairs in the current window using a hash map.

from collections import defaultdict

"""
Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.
"""


class Solution:
    def countGood(self, nums, k):
        mpp = defaultdict(int)
        ans = 0
        left = 0
        n = len(nums)
        pairs = 0
        for right in range(n):
            pairs += mpp[nums[right]]
            mpp[nums[right]] += 1

            while pairs >= k:  # shrink window
                ans += n - right
                mpp[nums[left]] -= 1
                pairs -= mpp[nums[left]]
                left += 1  # slide window
        return ans


s = Solution()
print(s.countGood([3, 1, 4, 3, 2, 2, 4], 2))
