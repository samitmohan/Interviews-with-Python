# https://leetcode.com/problems/type-of-triangle/description/?envType=daily-question&envId=2025-05-19


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)
        if a + b <= c:
            return "none"
        uniq = len(set(nums))
        if uniq == 1:
            return "equilateral"
        elif uniq == 2:
            return "isosceles"
        else:
            return "scalene"


s = Solution()
print(s.triangleType(nums=[3, 3, 3]))
print(s.triangleType(nums=[3, 4, 5]))
