# https://leetcode.com/problems/word-pattern/
# each characrter in pattern represents a word in s
# "this is" -> ['this', 'is]
# store it in dictionary as kv, key -> first set, val -> second set
# split and compare length of pattern and s (abba -> dog, cat, cat, dog)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        return len(set(zip(pattern, s))) == len(set(s)) and len(set(s)) == len(
            set(pattern)
        )
