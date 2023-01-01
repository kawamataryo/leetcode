#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        grid_length = len(grid)
        col_length = len(grid[0])
        for gi in range(grid_length):
            for ci in range(col_length):
                is_island = grid[gi][ci]
                if is_island:
                    result += 4
                if is_island and ci > 0 and grid[gi][ci - 1]:
                    result -= 2
                if is_island and gi > 0 and grid[gi - 1][ci]:
                    result -= 2
        return result
# @lc code=end
