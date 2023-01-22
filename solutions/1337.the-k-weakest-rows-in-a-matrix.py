#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        idx_and_sol = [(i, sum(row)) for i, row in enumerate(mat)]
        heapq.heapify(idx_and_sol)
        return [n[0] for n in heapq.nsmallest(k, idx_and_sol, key=itemgetter(1))]
# @lc code=end
