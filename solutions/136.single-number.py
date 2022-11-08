#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
            else:
                nums_set.add(num)
        return nums_set.pop()
# @lc code=end
