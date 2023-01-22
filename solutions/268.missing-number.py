#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from functools import reduce

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result


# @lc code=end
