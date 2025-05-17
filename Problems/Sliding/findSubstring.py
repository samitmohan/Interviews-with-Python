# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: order doesn't matter, foobar is in 0th posn (as barfoo) and 9th posn (as foobar)

# Hashmap of words : {foo : 1, bar : 1} [hm]
# Nested Sliding Window :
# ["foo", "bar"] : 3 * 2 = 6 : sliding window of 6
# inside the SW of 6 -> another sliding window block of 3 (per individual word)
# create hashmap : {foo : 1, bar : 1} and check with original hashmap of words hm : if same : append index in answer else move window
# {arf : 1, oot : 1} != hm hence shift window...

from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        hm = Counter(words)  # foo : 1, bar : 1
        ans = []
        i = 0
        j = (
            len(words[0]) * len(words) - 1
        )  # words = ["foo", "bar"] : len(words[0]) [foo] {3} * len(words) {2} = 6 : sliding window size
        # sliding window technique
        while j < len(s):
            # sub-sliding window a = start b = end posn
            a = i
            b = (
                i + len(words[0]) - 1
            )  # why i + ? :: b = foo (i = f, b = o) and then next a should be at bar : b and b at r
            # hashmap to compare
            temp_hm = {}
            while b <= j:
                if s[a : b + 1] in temp_hm:
                    temp_hm[s[a : b + 1]] += 1
                else:
                    temp_hm[s[a : b + 1]] = 1

                # sliding window shift
                a = b + 1
                b = b + len(words[0])

            # check original hashmap with temp hashmap
            if temp_hm == hm:
                # answer found
                ans.append(i)

            i += 1
            j += 1

        return ans
