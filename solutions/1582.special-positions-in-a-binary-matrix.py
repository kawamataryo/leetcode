#
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#

# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        tr_mat = list(zip(*mat))
        col_len = len(mat[0])

        ans = 0
        for row in mat:
            if sum(row) != 1:
                continue
            for i in range(col_len):
                if row[i] == 1 and sum(tr_mat[i]) == 1:
                    ans += 1
        return ans



# @lc code=end
