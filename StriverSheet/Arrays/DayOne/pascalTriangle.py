# https://takeuforward.org/data-structure/program-to-generate-pascals-triangle/
"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.
Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.
Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]

Example 2:

Input: numRows = 1
Output: [[1]]

Thinking-:
[[1]] -> curr + prevs
"""

from typing import List


def pascalTriangle(numRows: int) -> List[List[int]]:
    global ans
    ans = [[1]]
    for i in range(numRows - 1):
        # temp array -> left and right 0 to make calc easier
        temp = [0] + ans[-1] + [0]  # 0 1 0
        row = []
        # build new row
        for j in range(len(ans[-1]) + 1):
            # row
            row.append(temp[j] + temp[j + 1])
        ans.append(row)

    # variation 2
    # return ans[numRows - 1]
    return ans  # variation 3


# Better way is to use nCr formula


def nCr(n : int, r : int) -> float:
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)

    return res


def pascalTriangleVar1(r : int, c : int) -> int:
    element = nCr(r - 1, c - 1)
    return element
    global ans
    if len(ans) <= r:
        # Generate more rows if needed
        pascalTriangle(r + 1)  # This will update global ans

    # Check bounds
    if r < 0 or c < 0 or c >= len(ans[r]):
        return None  # or raise an exception

    return ans[r - 1][c - 1]


if __name__ == "__main__":
    print(pascalTriangle(5))
    print(pascalTriangleVar1(5, 3))

"""
Time Complexity : O(numRows^2)
Space Complexity : O(numRows^2)
"""
