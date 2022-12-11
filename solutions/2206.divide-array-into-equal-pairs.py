#
# @lc app=leetcode id=2206 lang=python3
#
# [2206] Divide Array Into Equal Pairs
#

# @lc code=start
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        result = 0
        for n in nums:
            result ^= n

        return result == 0
# @lc code=end
