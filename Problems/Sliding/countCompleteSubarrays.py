# https://leetcode.com/problems/count-complete-subarrays-in-an-array/?envType=daily-question&envId=2025-04-24
'''
Bruteforce - o(n^3)
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        complete_subarrays = 0
        subarrays = [arr[i:j+1] for i in range(len(nums)) for j in range(i, len(nums))]
        for subarray in subarrays:
            if set(subarray) == set(nums): 
                complete_subarrays += 1
        return complete_subarrays
        
This doesn't work on these constraints
    1 <= nums.length <= 1000
    1 <= nums[i] <= 2000

A better solution would be to use sliding window and keep increase the window and also check if they have distinct elements
at the same time (using a frequency counter)

Example Walkthrough

For nums =[1][3][1][2][2] (distinct count = 3):

    Expand the window until it contains all 3 distinct elements.

    Once valid, shrink the window from the left while maintaining validity. Each valid window contributes (n - right) subarrays to the total count.
    Each valid window will be from all left to right subarrays == len(nums) - right # standard sliding window

'''
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans, left, distinct_in_window = 0, 0, 0
        count = defaultdict(int)
        total_count = len(set(nums))
        
        for right in range(len(nums)):
            # update freq counter
            count[nums[right]] += 1
            if count[nums[right]] == 1:
                # it is a unique element
                distinct_in_window += 1
        
            # sliding window
            while distinct_in_window == total_count:
                # add to ans
                ans += len(nums) - right
                # shift window
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    distinct_in_window -= 1
                left += 1
        return ans
                
            
        

