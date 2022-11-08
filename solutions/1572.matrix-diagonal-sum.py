#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
import math

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)

        total = 0
        x = 0
        y = length - 1

        while x < length:
            total += mat[x][x]
            total += mat[y][x]
            x += 1
            y -= 1

        if length % 2 != 0:
            center = (length - 1) // 2
            total -= mat[center][center]

        return total



# @lc code=end
