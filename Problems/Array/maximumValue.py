# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/description/?envType=daily-question&envId=2025-05-23
from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        """

        Go through all edges -> bfs:
            Pick edge (u, v):
                curr_max = sum(nums)
                nums[u] ^= k
                nums[v] ^= k
                maxsum = max(sum(nums), curr_max)
            return maxsum

        This is the wrong approach, we can xor with k as many times as we want.
        What's the pattern here -:
            For each node, you have two possible values: nums[i] or nums[i] ^ k
            The question becomes: for each node, which value should you choose?

            You can only change a node's value if it's part of an edge that you "activate"
            If you activate an edge, both endpoints must be XORed with k

            Even number of nodes XORed: Pick the best even number of nodes to maximize the sum
            Odd number of nodes XORed: This is impossible, so this case contributes 0 to your answer

            Key observation in XOR : (n ^ k) ^ k will always be = n

            Instead of picking edges (which will not maximise it necessary since you get the same shit after xor) -> Pick any random nodes
            So once you xor any node, you must xor some other node too and your options are = without_xor, with_xor

            total = prevs sum
            Create delta array (by how much node val increases after xor) and take two at a time and see if their sum > 0: if yes -> add to total
            (Sort delta array in desc order) :: TC = (nlogn)
        """

        # Input: nums = [1,2,1], k = 3, edges = [[0,1],[0,2]] ||  Output: 6
        delta = [(n ^ k) - n for n in nums]  # [1,-1,1]
        delta.sort(reverse=True)  # [1,1-1]
        ans = sum(nums)
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                break  # can't xor odd
            new_ans = delta[i] + delta[i + 1]
            if new_ans < 0:
                break
            ans += new_ans
        return ans
