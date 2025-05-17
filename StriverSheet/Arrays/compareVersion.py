# https://leetcode.com/problems/compare-version-numbers/submissions/1626925414/?envType=problem-list-v2&envId=op9yyihc
from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """

        version1 = "1.2", version2 = "1.10"
        conversion1 = 12
        converstion2 = 110
        """
        # Converting to int deals with leading zeroes.
        v1_parts = [int(p) for p in version1.split(".")]
        v2_parts = [int(p) for p in version2.split(".")]
        # zip_longest takes care of unequal lengths.
        for p1, p2 in zip_longest(v1_parts, v2_parts, fillvalue=0):
            if p1 < p2:
                return -1
            elif p1 > p2:
                return 1
        return 0


def main():
    s = Solution()
    print(s.compareVersion(version1="1.2", version2="1.10"))  # -1
    print(s.compareVersion(version1="1.01", version2="1.001"))  # 0
    print(s.compareVersion(version1="1.0", version2="1.0.0.0"))  # 0


main()
