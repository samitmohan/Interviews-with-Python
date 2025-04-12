"""
Tim has N cupcakes, indexed from 0 to n - 1. Each cupcake has a prize money printed on it represented by an array nums. Tim wants to eat all the cupcakes.
If Tim eats ith cupcake, he will get nums[i-1 ]* nums[i] * nums[i+1] prize money. If i-1 or i+1 goes out of bounds of the array, then treat it as if there is a cupcake with a 1 printed on it.

Return the maximum prize money Tim can collect by eating all the cupcakes wisely.

Example 1 -:
Input :
nums = [1,5]
Output : 10

Explanation :
nums = [1,5] -> [5] -> []
coins = 1*1*5 + 1*5*1 = 10

Example 2 -:
Input: 
nums = [3,1,5,8]
Output: 167

Explanation:
nums = [3,1,5,8] -> [3,5,8] -> [3,8] -> [8] -> []
coins = 3*1*5 + 3 * 5 * 8 + 1*3*8 + 1*8*1 = 167

Input Explanation -: First line is the size of the array and the next line is the set of values.
Sample Input (Example 1):
2
1
5

Sample Output (Example 1): 
10
"""

# Burst Balloon

# Time : O(n^3)
# Space : O(n^2)

def maxCoins(nums):
    nums = [1] + nums + [1] # when we consider adjacent elements, we don't run into boundary issues
    dp = {}
    @cache
    def dfs(left, right): # current sub array being considered : left and right
        if left > right: return 0 # nothing to pop (no coins to collect since no elements left in subarray)
        if (left, right) in dp: return dp[(left, right)] # memo
        # computation
        dp[(left, right)] = 0
        # max points we can get for this pair
        for i in range(left, right + 1):
            coins = nums[left - 1] * nums[i] * nums[right + 1]
            # call for both left and right sub array
            coins += dfs(left, i - 1) + dfs(i + 1,m right)
            dp[(left, right)] = max(dp[(left, right)], coins)
        return dp[(left, right)]
    return dfs(1, len(nums) - 2) # ignore the last 1 added

# Tabluation
def maxCoins(nums):
    n = len(nums)
    # Extend the list 'a' with 1s at both ends
    nums.insert(0, 1)
    nums.append(1)

    # Create a 2D DP table initialized with 0s
    dp = [[0] * (n + 2) for _ in range(n + 2)]

    # Loop from the end of 'a' to the beginning
    for left in range(n, 0, -1):
        for right in range(1, n + 1):
            if left > right:
                continue
            maxi = float('-inf')
            
            # Iterate through the balloons from 'i' to 'j'
            for ind in range(left, right + 1):
                cost = nums[left - 1] * nums[ind] * nums[right + 1] + dp[left][ind - 1] + dp[ind + 1][right]
                maxi = max(maxi, cost)
            
            dp[left][right] = maxi
    
    return dp[1][n]