'''
https://leetcode.com/problems/count-of-interesting-subarrays
Subarray sum = k problem
'''

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = defaultdict(int)
        count[0] = 1 # prefix sum modulo is 0
        curr, ans = 0, 0
        for num in nums:
            if num % modulo == k: curr += 1
            target = (curr - k) % modulo
            # check if target in hm
            ans += count[target]
            # update freq of curr prefix mod
            count[curr % modulo] += 1
        return ans
