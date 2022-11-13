#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num_1 = num_2 = 0
        for n in nums:
            if n > num_1:
                num_2 = num_1
                num_1 = n
            elif n > num_2:
                num_2 = n
        return (num_1 - 1) * (num_2 - 1)
# @lc code=end
