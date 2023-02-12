#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#

# @lc code=start
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        transpose_matrix = list(map(list, (zip(*matrix))))

        ans = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                num = matrix[row][col]
                if num == min(matrix[row]) and num == max(transpose_matrix[col]):
                    ans.append(num)
                    break

        return ans
# @lc code=end
