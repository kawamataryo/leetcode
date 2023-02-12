#
# @lc app=leetcode id=2373 lang=python3
#
# [2373] Largest Local Values in a Matrix
#

# @lc code=start
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        local = []
        for row in range(1, len(grid) - 1):
            local_col = []
            for col in range(1, len(grid[0]) - 1):
                local_col.append(max(
                    grid[row-1][col-1],
                    grid[row-1][col],
                    grid[row-1][col+1],
                    grid[row][col-1],
                    grid[row][col],
                    grid[row][col+1],
                    grid[row+1][col-1],
                    grid[row+1][col],
                    grid[row+1][col+1],
                ))
            local.append(local_col)
        return local

# @lc code=end
