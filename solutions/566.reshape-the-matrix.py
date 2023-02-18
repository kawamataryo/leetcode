#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        mat_row_len = len(mat)
        mat_col_len = len(mat[0])
        if mat_row_len * mat_col_len != r * c:
            return mat

        ans = []
        mat_row_i = 0
        mat_col_i = 0
        max_row = mat_row_len - 1
        max_col = mat_col_len - 1
        for row in range(r):
            ans_col = []
            for col in range(c):
                if mat_row_i > max_row:
                    return mat
                ans_col.append(mat[mat_row_i][mat_col_i])
                if mat_col_i < max_col:
                    mat_col_i += 1
                else:
                    mat_col_i = 0
                    mat_row_i += 1
            ans.append(ans_col)

        return ans
# @lc code=end
