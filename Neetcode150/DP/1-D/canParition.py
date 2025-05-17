# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&t=3s


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False  # can't split if odd
        dp = set()
        dp.add(0)  # defai;t
        target = sum(nums) // 2
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False
