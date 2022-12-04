#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_count = {}
        for n in nums:
            if n in element_count:
                element_count[n] += 1
            else:
                element_count[n] = 1
            if element_count[n] > (len(nums) / 2):
                return n
# @lc code=end
