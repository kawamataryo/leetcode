#
# @lc app=leetcode id=1827 lang=python3
#
# [1827] Minimum Operations to Make the Array Increasing
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        operation_count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = (nums[i - 1] + 1) - nums[i]
                operation_count += increment
                nums[i] = nums[i] + increment

        return operation_count
# @lc code=end
