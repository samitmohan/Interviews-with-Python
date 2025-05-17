# https://leetcode.com/problems/pascals-triangle/
# O(n^2)
# Add 0s to begin and end for easier calculation


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows - 1):  # because 1 row made above
            # trick : old row = add 0 at begin and end (temp row
            temp = [0] + ans[-1] + [0]
            row = []
            for j in range(
                len(ans[-1]) + 1
            ):  # build next row : size = len(prevs_row + 1)
                row.append(temp[j] + temp[j + 1])
            ans.append(row)
        return ans
