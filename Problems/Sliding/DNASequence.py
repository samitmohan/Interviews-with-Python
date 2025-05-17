# https://leetcode.com/problems/repeated-dna-sequences/
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
"""
Sliding Window of 10, keep 2 hashsets : seen and ans, if 10 characters already in seen (repeats again) -> add to answer else first time seeing these 10 characters : add to seen hashset
"""


def findRepeatedDnaSequences(s):
    seen, ans = set(), set()
    for l in range(len(s) - 9):  # atleast 10 characters should be present
        curr = s[l : l + 10]  # sliding window range
        if curr in seen:
            ans.add(curr)
        else:
            seen.add(curr)
    return list(ans)  # convert to list


def main():
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(findRepeatedDnaSequences(s))


main()
