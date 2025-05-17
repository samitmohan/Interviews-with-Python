"""
https://leetcode.com/problems/count-subarrays-with-score-less-than-k/?envType=daily-question&envId=2025-04-28
Since constraints are large, can't use 2 ptr/sliding window
Best strategy would be to use a hashmap and precompute.
[1,2,3,4,5]

[1] = 1 * 1 = 1
[1,2] = 3 * 2 = 6
[1,2,3] = 6 * 3 = 18
[1,2,3,4] = 10 * 4 = 40
[1,2,3,4,5] = 15 * 5 = 75
Similarily for 2. This would also take too much space.

precomputed_arr = [1,6,18,40,75]
if precomputed_arr[i] < k: ans += 1

Scratch this.
Think of a hashmap.
1 -> tied to all scores of 1 ([1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5])
2 -> tied to all scores of 2 ([2], [2,3], [2,3,4], [2,4,5])
3 -> tied to all scores of 3 ([3], [3,4], [3,4,5])
4 -> tied to all scores of 4 ([4], [4,5])
5 -> tied to all scores of 5 [([5])]

run through the hashmap.values(), if any of them < k: ans += 1

Question is how do you tie 1 to all scores of 1?
{1 : [1, 6, 18, 40, 75]} # key(int) : val(list)
similarily for 2 -> {2 : [all scores of 2]}

How do you do list_of_scores_of_i here?
We know it'll be something like len(i) * sum(i) and we need to shift i (can use sliding window here?)
left, ans = 0, 0
hm = {}
for right in range(len(nums)) - 1:
    total += nums[left:right+1]
    length = right - left + 1
    score = total * length
    while score >= k:
        ans += length - right
        hm[left] -= nums[i]
        left += 1
    return ans
Actually we don't even need a hashmap
"""


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left, ans = 0, 0
        total = 0
        for right in range(len(nums)):
            total += nums[right]

            while total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            ans += right - left + 1
        return ans
