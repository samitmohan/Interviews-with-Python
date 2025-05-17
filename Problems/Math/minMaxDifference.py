# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description/
# Input: num = 11891
# Output: 99009
# Explanation:
# To achieve the maximum value, Danny can remap the digit 1 to the digit 9 to yield 99899.
# To achieve the minimum value, Danny can remap the digit 1 to the digit 0, yielding 890.
# The difference between these two numbers is 99009.

# For minimal value we always just replace first digit into zero:
# int(num.replace(num[0], "0").

# For maximum value - find first non-9 digit and replace it into 9.


def minMaxDifference(num):
    nums = str(num)
    i = 0
    while nums[i] == "9" and i < len(nums) - 1:
        i += 1
    return int(nums.replace(nums[i], "9")) - int(nums.replace(nums[0], "0"))


def main():
    print(minMaxDifference(90))


main()
