#
# @lc app=leetcode id=2357 lang=python3
#
# [2357] Make Array Zero by Subtracting Equal Amounts
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = len(nums_set)
        return count - 1 if 0 in nums_set else count
# @lc code=end
