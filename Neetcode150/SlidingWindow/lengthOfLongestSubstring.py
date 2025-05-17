# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window : remove left val, add right val and increment left pointer dynamically to check
        sett = set()  # to store val : no duplicates
        left, right = 0, 0
        ans = 0
        # standard SW code
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            # if not present : new val :: add to set
            sett.add(s[right])
            ans = max(
                ans, right - left + 1
            )  # r-l+1 denotes teh window size : length of the answer (abc) = 3
        return ans
