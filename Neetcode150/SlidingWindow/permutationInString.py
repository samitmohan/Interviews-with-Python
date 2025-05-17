# https://leetcode.com/problems/permutation-in-string/description/
"""
Same as find all anagrams
Steps:
  1. 2 hashmaps : hm_s1, hm_s2
  2. Sliding window : for first window if hm_s1 == hm_s2 -> True
  3. Else shift window : right += 1 and increment hm_s2[right] hashmap value to keep on checking
  4. left += 1 after window reached
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1, d2 = {}, {}
        if len(s1) > len(s2):
            return False
        # compute hashmap
        for i in range(len(s1)):
            d1[s1[i]] = 1 + d1.get(s1[i], 0)
            d2[s2[i]] = 1 + d2.get(s2[i], 0)

        if d1 == d2:
            return True
        left, right = 0, 0
        for right in range(len(s1), len(s2)):
            # shift window by one : add right's value to hashmap
            d2[s2[right]] = 1 + d2.get(s2[right], 0)  # same as hm (d2[s2[right] += 1])
            # decrement left value from hashmap and if value = 0 :: remove the character completely
            d2[s2[left]] -= 1
            if d2[s2[left]] == 0:
                d2.pop(s2[left])
            if d1 == d2:
                return True
            # else keep incrementing left pointer
            left += 1
        return False  # otherwise
