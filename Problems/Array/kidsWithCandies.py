# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
# Go through list and check for max number.
# O(N)
class Solution:
    def kidsWithCandies(candies, extraCandies):
        maxi = float("-inf")  # current maxi
        for i in range(len(candies)):
            if candies[i] > maxi:
                maxi = candies[i]

        ans = []
        for i in range(len(candies)):  # O(N)
            if candies[i] + extraCandies >= maxi:
                ans.append(True)
            else:
                ans.append(False)
        return ans


# One Liner


class Solution:
    def kidsWithCandies(candies, extraCandies):
        return [candy + extraCandies >= max(candies) for candy in candies]
