#
# @lc app=leetcode id=1260 lang=python3
#
# [1260] Shift 2D Grid
#

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1

        for _ in range(k):
            new_grid = []
            for row in range(max_row + 1):
                if row == 0:
                    new_grid.append([grid[max_row][max_col], *grid[row][:max_col]])
                    continue
                new_grid.append([grid[row - 1][max_col], *grid[row][:max_col]])
            grid = new_grid

        return grid





# @lc code=end
