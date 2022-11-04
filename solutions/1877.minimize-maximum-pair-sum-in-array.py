#
# @lc app=leetcode id=1877 lang=python3
#
# [1877] Minimize Maximum Pair Sum in Array
#

# @lc code=start
import math

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        result = 0
        for i in range(math.floor(len(nums) / 2)):
            result = max(result, sorted_nums[i] + sorted_nums[-(i+1)])
        return result

# @lc code=end
