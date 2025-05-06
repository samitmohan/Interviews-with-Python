# https://leetcode.com/problems/repeated-string-match/
'''
        minimum number of times a should be repeated st b is 
        substring of it.
        if impossible : return -1

        i want to repeat a st it matches string b
        "abcd"
        "ab|cd abcd ab|cd"
        "cdabcdab" : len = 8
        so atleast we need a to be 8
        until its 8 -> append the string again
        abcdabcd : now it's 8.
        now see if cdabcdab and abcdabcd ever match
        number left in right side of string (2 in this case) -> append abcd that many amount of times a[:2] like this
        assume b is longer than a.
        if len(b) < len(a): return -1

abcd : 4
cdabcdab : 8
abcdabcd ab left

I need to repeat 'a' enough times such that total length of a is atleast len(b)
repeat = ceil(len_b/len_a) 
so its either repeat or repeat+1 -> depending which case b becomes a substring.
repeat + 1
repeated_string = string  * repeat

if b in repeated_string: return repeat
'''
from math import ceil
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat = ceil(len(b) / len(a))
        repeat_new = repeat+1
        repeated_string = (a*repeat) # abcdabcd
        repeated_string_new = (a * repeat_new) # abcdabcdabcd
        if b in repeated_string: return repeat
        elif b in repeated_string_new: return repeat + 1
        return -1
s = Solution()
print(s.repeatedStringMatch("abcd", "cdabcdab"))
print(s.repeatedStringMatch(a = "a", b = "aa"))


