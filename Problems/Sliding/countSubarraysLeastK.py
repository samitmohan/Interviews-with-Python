# 2962. Count Subarrays Where Max Element Appears at Least K Times

# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        # now its just sliding window
        left = 0
        ans = 0
        count = 0
        for right in range(len(nums)):
            if nums[right] == max_num:
                count += 1
            while count >= k:
                ans += len(nums) - right
                if nums[left] == max_num:
                    count -= 1
                left += 1
        return ans
