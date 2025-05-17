"""
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/?envType=daily-question&envId=2025-04-30

I can go through each number -> maintain a count of len of that number in a hashmap, if that val is even -> ans++
hm = {12 : 2, 345 : 3, 2 : 1, 6 : 1, 7896 : 4}

OR

return sum(len(str(num)) % 2 == 0 for num in nums)


Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.

Example 2:

Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.



Constraints:

    1 <= nums.length <= 500
    1 <= nums[i] <= 105

"""


class Solution:
    def findNumbers(self, nums):
        hm = {}
        ans = 0
        for num in nums:
            hm[num] = len(str(num))
            if hm[num] % 2 == 0:
                ans += 1
        return ans


# This is so overkill, better solution


class Solution:
    def findNumbers(self, nums):
        return sum(len(str(num)) % 2 == 0 for num in nums)


s = Solution()
print(s.findNumbers(nums=[555, 901, 482, 1771]))
