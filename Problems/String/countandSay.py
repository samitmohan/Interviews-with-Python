# https://leetcode.com/problems/count-and-say/

"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
- countAndSay(1) = "1"
- countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
  which is then converted into a different digit string.

Example sequence:
1 -> "1"
2 -> "11" (one 1)
3 -> "21" (two 1s)
4 -> "1211" (one 2, one 1)
5 -> "111221" (one 1, one 2, two 1s)
"""


# https://leetcode.com/problems/count-and-say/

"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
- countAndSay(1) = "1"
- countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
  which is then converted into a different digit string.

Example sequence:
1 -> "1"
2 -> "11" (one 1)
3 -> "21" (two 1s)
4 -> "1211" (one 2, one 1)
5 -> "111221" (one 1, one 2, two 1s)
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        for i in range(1, n):
            current = ans[0]  # first
            count = 1  # "1" count is 1
            newdata = ""
            for digit in ans[1:]:
                if digit == current:
                    count += 1
                else:  # new digit -> update ans and reset count to 1
                    newdata += str(count) + current  # 11
                    current = digit
                    count = 1
            ans = newdata + str(count) + current  # for last
        return ans


s = Solution()
print(s.countAndSay(4))  # 1211
