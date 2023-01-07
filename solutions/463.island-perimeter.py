#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        max_row = len(grid)
        max_col = len(grid[0])

        self.ans = 0
        self.visited = set()

        def traverse_island(row: int, col: int):
            self.visited.add((row, col))
            # traverse top
            if row == 0:
                self.ans += 1
            else:
                if grid[row - 1][col]:
                    if (row - 1, col) not in self.visited:
                        traverse_island(row - 1, col)
                else:
                    self.ans += 1
            # traverse bottom
            if row == max_row - 1:
                self.ans += 1
            else:
                if grid[row + 1][col]:
                    if (row + 1, col) not in self.visited:
                        traverse_island(row + 1, col)
                else:
                    self.ans += 1
            # traverse left
            if col == 0:
                self.ans += 1
            else:
                if grid[row][col - 1]:
                    if (row, col - 1) not in self.visited:
                        traverse_island(row, col - 1)
                else:
                    self.ans += 1
            # traverse right
            if col == max_col - 1:
                self.ans += 1
            else:
                if grid[row][col + 1]:
                    if (row, col + 1) not in self.visited:
                        traverse_island(row, col + 1)
                else:
                    self.ans += 1

        for row in range(max_row):
            for col in range(max_col):
                if grid[row][col]:
                    traverse_island(row, col)
                    return self.ans

# @lc code=end
