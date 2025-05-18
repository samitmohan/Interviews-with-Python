# All Palindrome Partition Problems
# Problem 1
# https://leetcode.com/problems/palindrome-partitioning/

from functools import lru_cache

"""
Try all possible splits from the current index.
If a substring is a palindrome, add it to the current path.
Recursively explore the rest of the string.
Backtrack (undo the last choice) and try the next possibility.
"""


def partitionI(s: str):
    ans = []

    def ispal(s):
        return s == s[::-1]

    def helper(start, path):
        # base case
        if start == len(s):
            ans.append(path[:])
        # recursive case
        for i in range(start, len(s)):
            if ispal(s[start : i + 1]):
                path.append(s[start : i + 1])
                helper(i + 1, path)
                path.pop()

    helper(0, [])
    return ans


""" 
Return minimum number of cuts in palindrome partition

Input: "aab"
Valid palindrome partitions:
    ["a", "a", "b"] → 2 cuts
    ["aa", "b"] → 1 cut ✅ ← best

Output: 1 
"""


# Bruteforce
@lru_cache
def partitionII(s: str):
    def ispal(s):
        return s == s[::-1]

    def helper(start):
        if start == len(s):
            return 0  # no further partition

        mincuts = float("inf")
        for i in range(start, len(s)):
            if ispal(s[start : i + 1]):
                cuts = 1 + helper(i + 1)
                mincuts = min(cuts, mincuts)
        return mincuts

    return helper(0) - 1  # subtract 1 cuz of one extra cut at the end


# DP
""" 
Quick observation: for string of size n, if I make n-1 cuts -> every individual substring will be a palindrome
aabb -> a|a|b|b (3 cuts), aa | bb (1 cut), a|a|bb (2 cuts) -> min_cut = 1
Example -: s = bababcbadcede

Front parition idea -> partition first letter then see if you can parition rest
is b a palindrome? yes -> parititon -> b|ababcbadcede = 1 + (ababcbadcede)
is ba a palindrome? yes -> partition -> ba|babcbadcede = 1 + (babcbadcede)
is bab a palindrome? yes -> partition -> bab|abcbadcede = 1 + (abcbadcede)
is baba a palindrome? no
is babab a palindrome? no
is bababc a palindrome? no
is bababcb a palindrome? no
...
is bababcbadcede a palindrome? no

hence ans = min(1 + (ababcbadcede), 1 + (babcbadcede), 1 + (abcbadcede)) cuts. {each () gives you a number of cuts}
Example lets take 1 + (abcbadcede)

abcbadcede -> 1 (since a is pal) + (bcbadcede)
is abcba pal? yes -> partition = 1 + (dcede)

Writing Recurrance-:
1) Express everything in terms on idx (start from 0)
2) Express all possibilites
3) Take min of all possibilites 
4) Write base case

basically need i and j to iterate over the string
def helper(i, n, s):
    if i == n: return 0 # no partition
    mincost = inf {init}
    for (j = i, j < n; j++)  # b, ba, bab, baba, babab, bababc...
        temp += s[j]
        if ispal(temp):
            # can make a partition (cost = 1) and call for string j+1
            cost = 1 + helper(j + 1, n, s)
            mincost = min(cost, mincost)
    return mincost

Exponential Time Complexity -> there are overlapping subproblems -> apply memoization to recursion
What parameter is changing -> i {where we are placing the cut}
dp is 1D array
if dp[i] != -1: return
dp[i] = mincost

"""


def partitionIIDP(s: str):
    def ispal(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    # @lru_cache(maxsize=None) -> can use this and avoid dp arr
    def helper(i, n, s, dp):
        # base case
        if i == n:
            return 0  # no further partition
        if dp[i] != -1:
            return dp[i]

        mincuts = float("inf")
        for j in range(i, n):
            if ispal(i, j):
                cost = 1 + helper(j + 1, n, s, dp)
                mincuts = min(cost, mincuts)
        dp[i] = mincuts
        return dp[i]

    n = len(s)
    dp = [-1] * n
    return helper(0, n, s, dp) - 1  # why -1? cuz of one extra cut at the end


"""
Pretty straight forward, 2D DP
"""


def partitionIII(s, k):
    n = len(s)

    # This gives us the minimum number of changes to make s[i:j+1] a palindrome.
    def cost(i, j):
        substring = s[i : j + 1]
        return sum(substring[l] != substring[~l] for l in range(len(substring) // 2))

    @lru_cache(maxsize=None)
    def dp(i, k):
        # base case if no changes allowed
        if k == 0:
            return float("inf") if i < n else 0
        # n-i = number of char left in string starting from i, k = number of partitions we still need to make.
        # do we have enough characters left to form k partitions?
        if n - i < k:
            return float("inf")
        # recursive
        ans = float("inf")
        for j in range(i, n):
            ans = min(ans, cost(i, j) + dp(j + 1, k - 1))
        return ans

    return dp(0, k)


""" 
Given: A string s
Return True if it can be partitioned into three non-empty palindromic substrings, otherwise return False.

Input: "abcbdd"
Output: True
Explanation: "a" | "bcb" | "dd"

must split it into exactly three parts.
all three parts must be non-empty.
all three must be palindromes.

Brute Force (try all cuts):
    all possible ways to cut s into 3 substrings:
        Cut1: index i from 1 to n-2
        Cut2: index j from i+1 to n-1

s[:i], s[i:j], s[j:] = Check if all 3 parts are palindromes.
"""


# don't quite get this.
def partitionIV(s: str):
    n = len(s)
    ispal = [[False] * n for _ in range(n)]
    for i in range(n):
        ispal[i][i] = True  # single char is pal
    for i in range(n - 1):
        ispal[i][i + 1] = s[i] == s[i + 1]
    for length in range(3, n + 1):  # length of substring
        for i in range(n - length + 1):
            j = i + length - 1
            ispal[i][j] = s[i] == s[j] and ispal[i + 1][j - 1]

    # try all i, j to cut into 3 parts
    # i splits s[0:i]
    # j splits s[i:j]
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if ispal[0][i - 1] and ispal[i][j - 1] and ispal[j][n - 1]:
                return True
    return False


def main():
    # print(partitionI("aab"))
    # print(partitionII("aab"))
    # print(partitionII("a"))
    # print(partitionIIDP("ab"))
    # print(partitionIII("abc", 2))  # Output: 1
    # print(partitionIII("aabbc", 3))  # Output: 0
    print(partitionIV("abcbdd"))


main()
