# https://leetcode.com/problems/trapping-rain-water/

"""
Documentaion
  Should be boundary on left and right both and the area between them counts
  In order for boundary -> we must take minimum. 1 _ 2 -> _ can't be 2 (left boundary is 1, water will fall. take min(l, r) -> 1 unit)
  Take min(maximum left height, maximum right height) - height[current index we're at]
  No Water Trapped : min(l, r) - h[i] for ith position -> min(1,3), h[i] = 2, -> 1 - 2 = -1 (Can't trap neg number -> 0)
  Water Trapped : current height = 1, max_left = 2, max_right = 3, min(2,3) = 2 - 1 (height[i]) -> Trap 1 unit water in that position
  ---
  Find maxLeft, maxRight -> min(maxLeft, maxRight) -> How much water we can trap in that position
  For every single position -> Find how much water can be trapped for that position -> min(maxLeft, maxRight) - height[current_position]
"""


# Time complexity : O(N)


def trap(height):
    ans = 0
    left = 0
    right = len(height) - 1
    left_max, right_max = height[left], height[right]
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            ans += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            ans += right_max - height[right]
    return ans


def main():
    height = [4, 2, 0, 3, 2, 5]
    print(trap(height))


main()
