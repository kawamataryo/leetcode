#
# @lc app=leetcode id=1748 lang=python3
#
# [1748] Sum of Unique Elements
#

# @lc code=start
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        element_count_dict = {}
        for n in nums:
            if n in element_count_dict:
                element_count_dict[n] += 1
            else:
                element_count_dict[n] = 1
        return sum([ key for key, val in element_count_dict.items() if val == 1])
# @lc code=end
