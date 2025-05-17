# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
"""
Goal : smaller values : convert to target
Target : [2,7,5]
[1,8,4] : 8 is bigger than the value we're looking for.
So False :
    Observation : any triplet that has any single val > target triplet : false
Left inputs : [2,5,3], [1,7,5]
Go through triplet if target[i] in triplets : gurantee that somehow we can combine the triplets to target
Either equal or less than target.
1. Go through triplets, filter out values > target
2. Any of remaining triplets, can we reach target values (all 3) : True else False

Time : O(n)
"""


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()  # indices
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:  # 2 matches 2
                    good.add(i)
        return len(good) == 3
