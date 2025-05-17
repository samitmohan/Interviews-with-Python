# https://leetcode.com/problems/rearrange-array-elements-by-sign/

"""
Rules-:
    Every consecutive pair of integers have opposite signs.
    For all integers with the same sign, the order in which they were present in nums is preserved.
    The rearranged array begins with a positive integer.

[3,1,-2,-5,2,-4]
 l r

3 * 1 > 0 -> shift right

[3,1,-2,-5,2,-4]
 l    r

3 * -2 !> 0 -> add these two nums to new_arr
new_arr = [3,-2]
left += 1
right +=1

[3,1,-2,-5,2,-4]
   l    r

1 * -5 !> 0 -> add these two nums to new_arr
new_arr = [3,-2, 1, -5]

left += 1
right +=1

[3,1,-2,-5,2,-4]
      l    r

-2 * 2 -> yes -> add
[3,-2,1,-5,-2,2]


[3,1,-2,-5,2,-4]
         l    r

First approach
for left in range(len(nums)):
    for right in range(i+1, len(nums)):
        if nums[left] > 0 and nums[right] > 0:
            right += 1
        elif nums[left] < 0 and nums[right] < 0:
            left += 1

        # not pos -> nums[i]
        new_arr.append(nums[i], nums[j])
        left += 1
        right += 1

Too much thinking just seperate the positives and negatives

two pointer approach
while i < len(pos) and j < len(neg):
    ans.append(pos[i])
    ans.append(neg[j])
    i += 1
    j += 1
"""

from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [n for n in nums if n > 0]
        neg = [n for n in nums if n < 0]
        n = len(nums)
        ans = []
        for p, n in zip(pos, neg):
            ans.append(p)
            ans.append(n)
        return ans


s = Solution()
print(s.rearrangeArray([3, 1, -2, -5, 2, -4]) == [3, -2, 1, -5, 2, -4])
print(s.rearrangeArray([-1, 1]) == [1, -1])
