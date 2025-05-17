# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/

# https://www.youtube.com/watch?v=MOeuK6gaC2A&list=PLot-Xpze53leOBgcVsJBEGrHPd_7x_koV&index=9
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        alt1, alt2 = "", ""
        for i in range(len(s)):
            alt1 += "0" if i % 2 else "1"
            alt2 += "1" if i % 2 else "0"
        minflips = float("inf")
        diff1, diff2, left = 0, 0, 0
        for right in range(len(s)):
            # calculate differences between alternate and string
            if s[right] != alt1[right]:
                diff1 += 1
            if s[right] != alt2[right]:
                diff2 += 1
            # if sliding window bound reached (size : r-l+1)
            if (right - left + 1) > n:
                # subtract left value from both alt1 and alt2 (only if they're not equal)
                if s[left] != alt1[left]:
                    diff1 -= 1
                if s[left] != alt2[left]:
                    diff2 -= 1

                # shift left pointer by 1
                left += 1

            # ans
            if (right - left + 1) == n:
                minflips = min(minflips, diff1, diff2)
        return minflips
