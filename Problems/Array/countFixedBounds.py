'''
https://leetcode.com/problems/count-subarrays-with-fixed-bounds/?envType=daily-question&envId=2025-04-26
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

Idea : Keep a counter of values in hashmap.
Go through the nums -> if index i = maxK, check if minK exists in hashmap yet (on the left side) -> if yes ans += 1 else keep iterating
                
The number of valid subarrays equals the number of elements between invalid_index and the smaller of the two most recent positions.
        ans = 0
        last_minK, last_maxK, last_invalid = -1, -1, -1
        # need to keep track of these ^ (indices)
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                last_invalid = i # invalidates current window
            if nums[i] == minK: last_minK = i
            if nums[i] == maxK: last_maxK = i
            # if both last_minK and last_maxK are after last_invalid then valid subarray ends at i
            if last_invalid < last_minK and last_invalid < last_maxK:
                ans += max(0, min(last_minK, last_maxK) - last_invalid) # number of valid subarrays ending at index i (start after last_invalid and end at i)
        return ans        
'''
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        currMin = currMax = invalid_index = -1
        ans = 0
        for i, number in enumerate(nums):
            if number < minK or number > maxK: # out of bounds
                invalid_index = i
            if number == minK: currMin = i
            if number == maxK: currMax = i
            ans += max(0, min(currMin, currMax) - invalid_index)
        return ans

