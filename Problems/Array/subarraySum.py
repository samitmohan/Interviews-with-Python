# https://leetcode.com/problems/subarray-sum-equals-k/
# https://www.youtube.com/watch?v=fFVZt-6sgyo&t=606s

# Hashmap : prefix_sum and count and simple sliding window
# Not intuitive, think of hashmap and difference and removing extra work
# O(n)
# repetition allowed


class Solution:
    def subarraySum(nums, k):
        ans = 0
        curr_sum = 0
        prefix_sum = {
            0: 1
        }  # empty subarray by default (key = sum, value = number of times sum present)
        for n in nums:
            curr_sum += n
            diff = curr_sum - k
            ans += prefix_sum.get(diff, 0)
            prefix_sum[curr_sum] = 1 + prefix_sum.get(
                curr_sum, 0
            )  # update hashmap (sum : count)
        return ans


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(Solution.subarraySum(nums, k))
