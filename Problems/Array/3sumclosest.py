# https://leetcode.com/problems/3sum-closest/description/


def threeSumClosest(nums, target):
    nums.sort()
    result = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        low = i + 1
        high = len(nums) - 1
        while low < high:
            sum = nums[i] + nums[low] + nums[high]
            if sum == target:
                return sum
            if abs(sum - target) < abs(result - target):
                result = sum
            if sum < target:
                low += 1
            elif sum > target:
                high -= 1
    return result


def main():
    print(threeSumClosest([-1, 2, 1, -4], 1))  # 2


main()
