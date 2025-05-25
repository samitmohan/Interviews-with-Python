# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/?envType=daily-question&envId=2025-05-25

from typing import List
from collections import defaultdict


def longestPalindrome(words: List[str]) -> int:
    ans = 0
    hm = defaultdict(int)

    # for palindromes (lc, cl)
    for word in words:
        rev_word = "".join(reversed(word))
        if hm[rev_word] > 0:
            ans += 4
            hm[rev_word] -= 1
        else:
            hm[word] += 1

    # one more case: for same alphabets: aa, zz (which can be used in middle as palindrome)
    for word in hm:
        first_char, second_char = word[0], word[1]
        if hm[word] > 0 and first_char == second_char:
            ans += 2
            break

    return ans


def main():
    print(longestPalindrome(["lc", "cl", "gg"]))  # 6
    print(longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]))  # 10
    print(longestPalindrome(["cc", "ll", "xx"]))  # 8


main()
