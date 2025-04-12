"""
Aditya is playing a game on the computer where in each round he is given 2 strings out of which one string contains '*' and '?' in it. 
The task of aditya is to find out whether string contains '*' and '?' matches with the other string completely or not, there are some rules as follows to match the strings -:
  1) '?' matches any single character
  2) '*' Matches any sequence of characters (including empty sequence)

Identify if the two string matches or not using the above two conditions.

Note : Both the strings should match completely.

Example 1 -:
Input : str = "aaa", pattern = "*"
Output : Match
Explanation : '*' can match any sequence of characters.

Example 2 -:
Input : str = "abcd", pattern = "a?cc"
Output : Does not match
Explanation : '?' matches with 'b' but after that the characters are not matching.

Example 3 -:
Input : str = "abceb", p = "*a*b"
Output : Match
Explanation : The first '*' matches the empty sequence, while the second '*' matches the substring 'dce'

Input Explanation : First line is the string and second line is the pattern.

Sample Input (Example 1):
aaa
*

Sample Output (Example 1):
Match
"""

"""
Answer
set dp array to (m+1) * (n+1) where m, n are len of string and pattern resp.
case 1 : empty string, any pattern will match : dp[0][0] = True

"""
# Time : O(m * n)
# Space : O(m * n)

def isMatch(s, p):
    m, n = len(s), len(p)
    # 2d boolean array dp with dimensions (m+1)x(n+1).
    # dp[i][j] will represent whether the substring of s up to length i matches the substring of p up to length j.
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True  # empty string and pattern match by default

    # for '*'
    for j in range(1, n + 1):  # iterates through pattern string p
        if p[j - 1] == "*":  # current char in pattern p[j-1] is '*'
            # if yes : dp[0][j] = True if prevs char in pattern matches empty sequence
            dp[0][j] = dp[0][j - 1]  # dp[0][1] = dp[0][0] = True

    # loop through input string 's'
    for i in range(1, m + 1):
        for j in range(1, n + 1):  # iterates through characters of pattern 'p'
            # curr char in patern is either ? (matching any char) or if curr char in s marches curr char in pattern p :: if either true  = dp[i][j] = true if s and p string matches till ith and jth
            if p[j - 1] == "?" or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # matches that character
            elif p[j - 1] == "*":  # if curr char is '*'
                # sets dp[i][j] = true if * char matches sequence of char in inp string (dp[i-1][j]) or matches empty string dp[i][j-1]
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]  # can match any character
    return dp[m][n]


# dp = [[True, False], [False, True], [False, False], [False, False]]
# dp[3][1]

s = input()
p = input()

if isMatch(s, p):
    print("match")
else:
    print("no match")
