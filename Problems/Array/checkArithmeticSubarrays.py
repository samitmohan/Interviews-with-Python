# https://leetcode.com/problems/arithmetic-subarrays/
from typing import List

'''
nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
l is the starting range
r is the number of numbers to go from l
ans = []
from l to r in nums:
    [4,6,5] is the subarray
    sort -> 4,5,6
    now check if difference between nums is same
    if subarray[i+1] - subarray[i] = subarray[1] - subarray[0]:
        ans.append(true)
    else:
        ans.append(false)

Step1) Figure out how to get the subarray [4,6,5]
'''
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for left, right in zip(l, r):
            subarray = nums[left:right + 1]
            sorted_nums = sorted(subarray)
            diff = sorted_nums[1] - sorted_nums[0]
            for i in range(1, len(sorted_nums)):
                if sorted_nums[i] - sorted_nums[i-1] != diff:
                    res.append(False)
                    break
            else:
                res.append(True)
        return res

s = Solution()
print(s.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]))
print(s.checkArithmeticSubarrays(nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]))
        