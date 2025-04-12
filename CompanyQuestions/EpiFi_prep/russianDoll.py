# O(N^2)
# We can simple reverse sort the height if two width are equal, to remove duplicacy.
# the next coming height would be less than the previous one

class Solution:
    def maxEnvelopes(self, envelopes):
        # sort envelopes in ascending order of width and descending order of height
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # initialize an array to store the LIS of heights
        dp = [1] * len(envelopes)

        # find the LIS of heights
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # return the maximum LIS of heights
        return max(dp)


# O(n * log(n))) Optimised


# For each envelope, we get its height and use binary search to find the index where we can insert the current height to maintain the sorted order of the doll set.

# If the index is beyond the length of the doll set, we add the height to the end of the doll set.

# Otherwise, we replace the height at that index with the current height, since it can fit inside the previous envelope.

# We can make the above code more concise by using a python library bisect_left to locate the insertion point in the sort order.


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        res = []
        # Perform LIS
        for _, h in envelopes:
            l, r = 0, len(res) - 1
            # find the insertion point in the Sort order
            while l <= r:
                mid = (l + r) >> 1
                if res[mid] >= h:
                    r = mid - 1
                else:
                    l = mid + 1
            idx = l  # append at left
            if idx == len(res):  # if at end (append height at end)
                res.append(h)
            else:
                res[idx] = h  # else enter at position idx
        return len(res)
