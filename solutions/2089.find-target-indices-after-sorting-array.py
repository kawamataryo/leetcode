#
# @lc app=leetcode id=2089 lang=python3
#
# [2089] Find Target Indices After Sorting Array
#

# @lc code=start
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        under_count = 0
        same_count = 0
        for num in nums:
            if num == target:
                same_count += 1
            if num < target:
                under_count += 1

        return [i + under_count for i in range(same_count)]
# @lc code=end
