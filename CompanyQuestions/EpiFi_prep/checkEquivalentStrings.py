# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/description/
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        f1, f2 = [0] * 26, [0] * 26
        for ch in word1:
            f1[ord(ch) - ord('a')] += 1
        for ch in word2:
            f2[ord(ch) - ord('a')] += 1

        for i in range(26):
            if abs(f1[i] - f2[i]) > 3:
                return False
        return True


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d = {}
        for ch in word1:
            d[ch] = d.get(ch, 0) + 1
        for ch in word2:
            d[ch] = d.get(ch, 0) - 1
        difFreq = max(abs(val) for val in d.values())
        return difFreq <= 3


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d = Counter(word1)
        for ch in word2:
            d[ch] -= 1
        return max(abs(val) for val in d.values()) <= 3
