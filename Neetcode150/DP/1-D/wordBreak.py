# https://leetcode.com/problems/word-break/description/
"""
s = "leetcode"
["leet", "code]

check for l then le then lee and once first word formed, check for c then co...
O(n^2)

Optimised : O(n)

Decision Tree -> Cache -> DP

i = 0
s = "leetcode"
i = 4 is the sub problem
            i = 0
            /    \
        leet    code 
        /  \
      leet  code
Matched! i = 0 then i = 4 then i = 8. (8 is the length : Base case : true)

s = "neetcode" and word_dict - ["neet", "leet", "code"]

dp[8] = True
dp[7] = e---? False
dp[6] = False
dp[5] = False
dp[4] = code (matched word_dict) True
dp[3] = t-- False dp[2] = etco? False dp[1 = False]
dp[0] = True

so dp[0] matches and dp[4] also true (leet + code) Hence True
dp[0] = dp[0 + len(w)] = dp[0 + 4] = True

"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # there are enough characters in s to compare to
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break  # even if 1 word matches = True
        return dp[0]
