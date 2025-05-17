# https://leetcode.com/problems/minimum-window-substring/

# https://www.youtube.com/watch?v=DfljaUwZsOk : DIFFICULT PROBLEM : revisit


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        ans, minLength = [-1, -1], float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (right - left + 1) < minLength:
                    ans = [left, right]
                    minLength = right - left + 1
                # pop from the left of our window
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = ans
        return s[left : right + 1] if minLength != float("infinity") else ""
