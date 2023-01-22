#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        col_last_index = len(grid[0]) - 1
        row, col = 0, col_last_index
        row_length = len(grid)

        negative_count = 0
        while row < row_length:
            while col >= 0 and grid[row][col] < 0:
                negative_count += 1
                col -= 1
            col = col_last_index
            row += 1

        return negative_count
# @lc code=end
