# https://leetcode.com/problems/longest-repeating-character-replacement/
"""
standard sliding window technique
1. hashmap to keep count of alphabets in our window
2. sliding window : if window not valid : shift left pointer by one and also decrement hashmap value of left by one (update)
  . is valid? size of window - max value of hashmap <= k
  . not valid? sizeWindow (r-l+1) - max(hm.values()) > k
3. if valid : ans = max(ans, window size) : return ans (since we have to return length of longest substring = length of window = window size)

"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        ans = 0
        left, right = 0, 0
        for right in range(len(s)):
            # compute hashmap
            hm[s[right]] = 1 + hm.get(s[right], 0)
            # while window is invalid
            while (right - left + 1) - max(hm.values()) > k:
                hm[s[left]] -= 1
                left += 1
            # valid window
            ans = max(ans, right - left + 1)
        return ans
