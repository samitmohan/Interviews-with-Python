# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        # go till o (leetcode) no need to check de)
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


# Can also do KMP : compute LPS and match


class Solution:
    def strStr(self, text: str, pattern: str) -> int:
        if pattern == "":
            return 0
        lps = [0] * len(pattern)
        prev_lps, i = 0, 1
        while i < len(pattern):
            if pattern[i] == pattern[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps += 1
                i += 1
            elif prev_lps == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]  # prefix

        # matching
        i = 0  # ptr for text
        j = 0  # ptr for pattern
        while i < len(text):
            if text[i] == pattern[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]  # stored result
            if j == len(pattern):  # finished
                return i - len(pattern)
        return -1  # not found
