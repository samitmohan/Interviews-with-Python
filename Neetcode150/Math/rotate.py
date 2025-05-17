# https://leetcode.com/problems/rotate-image/description/


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 2 steps : Transpose Vector and Reverse the transposed vector.
        # 1. Transpose : row becomes col and col becomes row
        rows, cols = len(matrix), len(matrix[0])
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # swap

        # 2. Reverse transposed vector (just like array reverse : two pointers)
        for i in range(len(matrix)):
            low, high = 0, len(matrix[i]) - 1
            while low < high:
                # swap first and last row
                matrix[i][low], matrix[i][high] = matrix[i][high], matrix[i][low]
                low += 1
                high -= 1
