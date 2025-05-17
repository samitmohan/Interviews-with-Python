# https://leetcode.com/problems/regular-expression-matching/
# https://www.youtube.com/watch?v=HAA8mgxlov8
"""
If 2 special characters not present : regular string match
if "a." compare it to "aa" since "." can be any character.
    "a." and "ab" also matches. but "a.." and "aa" = False
"a*" means character present before it can be repeated 0 -> infinite times
    =  [" ", "a", "aa", "aaa" ....]

"ab" = ".*" = ["", ., .. and so on] {one of the dots can be a and b}

Start from empty string, two choices : * or . [decision tree]
2 decisions, repeating n times (input string) = 2^n

With cache : O(n * m) or n^2
Top-Down
aab and c*a*b
i       j
Decision Tree
        .
      /  \
    c    " "
2nd choice better, i is unchanged, j += 2 (no need for * because we will never repeat c as it doesn't match first string)
    (i, j + 2)

aab and c*a*b [right after j there is a star that means "a" can be repeated 0 / more times]
i         j

        .
      /  \
    c    " "
        /  \
       *    " "
       a
now a matches (j matches i), i += 1 and j remains same (as it can be repeated since * is the next char)
    (i + 1, j)

in the end
aab and c*a*b
  i         j
s[i] == p[j] = (i + 1, j + 1)
aab  and c*a*b
   i          j

if i out of bounds but j in bounds
    a and a*b* :: Technically it does match
but if j out of bounds but i in bounds : doesn't work : must return false

Both out of bounds : Pattern has matched : return True
"""

from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # top down memoization
        dp = {}

        @cache
        def backtrack(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            # i can be out of bounds still
            # match between first character
            match = i < len(s) and (
                s[i] == p[j] or p[j] == "."
            )  # . matches to any character

            # * has the highest precedence and first char in j can never be star
            # can only use * if there is a match
            if (j + 1) < len(p) and p[j + 1] == "*":
                dp[(i, j)] = (
                    backtrack(i, j + 2)  # don't use the *
                    or (match and backtrack(i + 1, j))
                )  # use the *
                return dp[(i, j)]

            if match:
                dp[(i, j)] = backtrack(i + 1, j + 1)
                return dp[(i, j)]

            dp[(i, j)] = False

            return False  # otherwise

        return backtrack(0, 0)
