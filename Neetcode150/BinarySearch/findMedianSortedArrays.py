# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/3162206/python-ez-code-binary-search-o-logn-runtime-explained/
# Difficult Problem : revisit
# https://www.youtube.com/watch?v=q6IEA26hvXckj

# Time: log(min(n, m))


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Binary Search only on A (A  : smaller of the two arrays)
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:  # median is guarenteed
            i = (l + r) // 2  # A
            j = (
                half - i - 2
            )  # B (why -2? j is the index of mid point (arrays are indexed at 0, j starts at 0))

            # correct left partition
            # these indices can be out of bounds : default val : -infinity and infinity
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
