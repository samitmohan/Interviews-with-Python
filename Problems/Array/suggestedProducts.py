# https://leetcode.com/problems/search-suggestions-system/
"""
Alphabetical order? sorted. O(nlogn)
Prefix Tree / Trie works but better solution : Two Pointers
Eliminate words : never consider them again
Words that match prefix will always be next to each other because they are sorted.

- Go character by character (does it have m (do both for L and R pointer))
[
L    mobile
    moneypot
    monitor
    mouse
R    mousepad
]
L[i] == m and R[i] == m so words in between them : also match : return 3 lexicographically (top 3 elements from L)
Return sublist
"""


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        ans = []
        products.sort()
        L, R = 0, len(products) - 1
        for i in range(len(searchWord)):
            char_to_compare = searchWord[i]
            # eliminate words not in prefix
            # product doesn't have ith character or ith character is not equal to character we are looking for
            while L <= R and (
                len(products[L]) <= i or products[L][i] != char_to_compare
            ):
                L += 1
            while L <= R and (
                len(products[R]) <= i or products[R][i] != char_to_compare
            ):
                R -= 1

            # valid answers
            ans.append([])
            remain = R - L + 1  # window of our answers
            for j in range(min(3, remain)):
                ans[-1].append(products[L + j])
        return ans
