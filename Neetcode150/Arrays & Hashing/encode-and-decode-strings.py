# https://leetcode.com/problems/encode-and-decode-strings/ (facebook)

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Example :: ["neetco#de"] -> encoded_string -> 4#neet5#co#de -> decoded_string = "neetco#de"


class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + "#" + s for s in strs)

    def decode(self, s: str) -> List[str]:
        # read the number fore # to know length of next word
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # 4
            word = s[j + 1 : j + 1 + length]
            ans.append(word)
            i = j + 1 + length  # next word in string
        return ans


"""
Documentation
  pick a delimiter : #. But what if # already present (sami#t mohan) -> sami t mohan (instead of samit mohan)
  need 2 delimiter -> len of string and #
  neet, co#de -> 4#neet, 5co#de
  always going to be an integer (len) before the string followed by delimiter (#) -> read 4 letters after # and remove delimiter.

Time Complexity :  O(N) -> N = total number of characters


def encode(strs):
    res = ""
    for s in strs:
        # encode
        res += str(len(s)) + "#" + s  # 4#neet
    return res

[4#leet]
    j
    ans.append(s[j + 1, j + 1 + length])
"""
