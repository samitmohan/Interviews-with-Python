# https://leetcode.com/problems/hand-of-straights/
"""
1 is always going to minimum in Example 1.
Can't form [0,1,2] : 1,2,3 -> 1 always at first position
Greedy about minimum value
Keep counter (hm)
-> Size of input array should be divisible by 3
-> Find minimum value (hm) and add to answer, find next minimum value, update hashmap after using
Group 1 formed : [1,2,3]
Counter : {1 : 0, 2 : 1, 3 : 1} :: min_val = 2.
Group 2 : [2,3,4]

We can find minimum in O(n) time, can we do better? Add keys to min heap.
    If count decremented to 0, pop from min heap.

Return false if consecutive value not present.
---Edge Case---
[1,1,3,6,2,3,4,7,8] : Counter : {1 : 2, 2 : 1, 3: 2...}
Group 1 : [1,2,3]
Group 2 : 1 is present (minVal) but 2 isnt. So pop from heap 2?? Can't pop arbitary number, can only pop minVal (1) :
But in this case if we have 1 and not 2 : we've already lost, so pop both items. New Counter : {3 : 1, 4 : 1} so on (can't pop not min val : return false)

T : log(n) (to find min) * n (times we're going to pop) : O(n * log(n))
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
"""

import heapq


class Solution:
    def isNStraightHand(hand, groupSize):
        if len(hand) % groupSize:  # > grpSize (can't be divided : 10/3)
            return False

        count = {}
        for x in hand:
            count[x] = 1 + count.get(x, 0)
        # heap
        min_heap = list(count.keys())
        heapq.heapify(min_heap)  # O(n)
        while min_heap:
            min_val = min_heap[0]
            for i in range(min_val, min_val + groupSize):
                if (
                    i not in count
                ):  # min val isn't present in hashmap (value isn't available)
                    return False
                # else decrement count of hashmap
                count[i] -= 1
                if count[i] == 0:  # eliminate value from heapq also : EDGE CASE
                    if (
                        i != min_heap[0]
                    ):  # {1 : 0, 2 : 1} so can't process 2 also : False
                        return False
                    heapq.heappop(min_heap)
        return True


if __name__ == "__main__":
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3
    print(Solution.isNStraightHand(hand, groupSize))
