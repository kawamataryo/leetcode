#
# @lc app=leetcode id=2319 lang=python3
#
# [2319] Check if Matrix Is X-Matrix
#

# @lc code=start
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        max_col = len(grid[0]) - 1
        x, y = 0, max_col

        for row in range(len(grid)):
            for col in range(max_col + 1):
                if col == x or col == y:
                    if grid[row][col] == 0:
                        return False
                else:
                    if grid[row][col] != 0:
                        return False
            x += 1
            y -= 1
        return True
# @lc code=end
