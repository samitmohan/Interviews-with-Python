# https://leetcode.com/problems/search-a-2d-matrix/description/
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

"""
BS1
  if target < matrix[row][0] (min value of that row : leftmost) :: look up
  if target > matrix[row][-1] (max value of that row : rightmost) :: look down
BS2
  if target > matrix[row][mid] :: look left
  if target < matrix[row][mid] :: look right
"""


def searchMatrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    # Binary Search to find in which row the target is in.
    top, bottom = 0, rows - 1
    while top <= bottom:
        row = (top + bottom) // 2
        if target < matrix[row][0]:
            bottom = row - 1
        elif target > matrix[row][-1]:
            top = row + 1
        else:
            break  # row found
    # if top > bottom :: return False (edgecase)
    if not (top <= bottom):
        return False

    row = (top + bottom) // 2  # row found position

    # Binary Search to find target in the specific row (values)
    low, high = 0, cols - 1
    while low <= high:
        mid = (low + high) // 2
        if target > matrix[row][mid]:
            low = mid + 1
        elif target < matrix[row][mid]:
            high = mid - 1
        else:
            return True
    return False  # otherwise


def main():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(searchMatrix(matrix, target))


main()
