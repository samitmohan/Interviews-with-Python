class Solution:
    '''
    Given -> A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
    len(nums) = len(ans)
    ans[i] = nums[nums[i]]

    '''
    def buildArray(self, nums):
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans

s = Solution()
print(s.buildArray(nums = [0,2,1,5,3,4]))
print(s.buildArray(nums = [5,0,1,2,3,4]))


# Without using space-:
def buildArray(nums):
    '''
    [0,2,1,5,3,4] =  nums[nums[0]], nums[nums[1]], nums[num[2]], nums[num[3]], nums[nums[4]], nums[nums[5]] = 
        nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]
        0, 1, 2, 4, 5, 3

    we need to enable each element nums[i] in nums to store both the 'current value' (i.e., nums[i]) and the 'final value' (i.e., nums[nums[i]]).
    range of val of nums = [0, 999] : 100 based system -> nums // 1000 = final_val, nums % 1000 = curr_val
    Traverse nums -> Calculate final_val of each element -> Add 1000 times that val to element.
    Then, we traverse the array again, and divide the value of each element by 1000, retaining the quotient.
    '''

    n = len(nums)
    for i in range(n):
        nums[i] += 1000 * (nums[nums[i]] % 1000)
    for i in range(n):
        nums[i] //= 1000
    return nums
    


def main():
    print(buildArray(nums = [0,2,1,5,3,4]))
main()

