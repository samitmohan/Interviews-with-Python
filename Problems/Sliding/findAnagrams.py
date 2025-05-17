# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""
To find anagram : count characters (hm) to check anagram or not and perform sliding window (find substrings)

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
size of p = 3
pcount = {a:1, b:1, c:1}
scount for 3 = {c:1,b:1,a:1}
  both hashmaps are same -> anagram found -> add index to answer.
Shift window : remove first letter (c) pop and add next letter (e) to scount
  Keep doing this until left and right pointer are at b and c respectively : anagram found at index 6 -> add
"""


def findAnagrams(s, p):
    if len(p) > len(s):
        return []
    # comparing hashmaps
    pcount, scount = {}, {}
    # scount =  {'a': 1, 'b': 1, 'c': 1}
    # pcount = {'c': 1, 'b': 1, 'a': 1}
    for i in range(len(p)):
        # dictionary.get(keyname, value) returns val for key and value = value to return if specified key does not exist (optional)
        scount[s[i]] = 1 + scount.get(s[i], 0)
        pcount[p[i]] = 1 + pcount.get(p[i], 0)

    ans = [0] if scount == pcount else []  # first index added if matched
    # sliding window
    left, right = 0, 0
    for right in range(
        len(p), len(s)
    ):  # start from len(p) to end (len(s)) = why not from 0 :: we already calculated answer for that ^
        # add right index, subtract left index (if count = 0 in hm : pop)
        scount[s[right]] = 1 + scount.get(s[right], 0)  # same as hm, default val = 0
        scount[s[left]] -= 1
        if scount[s[left]] == 0:
            scount.pop(s[left])
        # increment left pointer
        left += 1
        if scount == pcount:
            ans.append(left)
    return ans


def main():
    s = "cbaebabacd"
    p = "abc"
    print(findAnagrams(s, p))


main()
