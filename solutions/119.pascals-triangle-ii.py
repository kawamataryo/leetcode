#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prevRow = self.getRow(rowIndex - 1)

        inner_row = []
        for i in range(1, len(prevRow)):
            inner_row.append(prevRow[i - 1] + prevRow[i])

        return [1] + inner_row + [1]

# @lc code=end
