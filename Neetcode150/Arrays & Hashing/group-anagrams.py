# https://leetcode.com/problems/group-anagrams/

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))  # actostpostp
            ans[sorted_s].append(s)
        return list(ans.values())


s = Solution()
print(s.groupAnagrams(["act", "stop", "post", "hat"]))
