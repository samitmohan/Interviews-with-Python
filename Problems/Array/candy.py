# https://leetcode.com/problems/candy/submissions/

'''
Give every child 1 candy.
Traverse from L -> R :: if ratings[i] > ratings[i-1]: candies[i] = candies[i-1] + 1
Traverse from R -> L :: if ratings[i] > ratings[i+1]: 
    if candies[i] <= candies[i+1]: # only incremenet if candies[i] is lesser than neighbor
        candies[i] = candies[i+1] + 1
During the second traversal , we can observe that changing the values of arr doesn't affects the relation maintained in the first traversal

# candies = [1,1,1]
# [1, 0, 2] : after left pass [1, 1, 2] -> after right pass [2, 1, 2] 
'''
class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n
        # left traversal
        for i in range(1, n):
            if ratings[i] > ratings[i-1]: 
                candies[i] = candies[i-1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                if candies[i] <= candies[i+1]: candies[i] = candies[i+1] + 1
        return sum(candies)


s = Solution()
print(s.candy([1,0,2]))