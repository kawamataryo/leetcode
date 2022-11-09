#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        non_duplicate = 0
        for n in nums:
            non_duplicate ^= n
        return non_duplicate
# @lc code=end
