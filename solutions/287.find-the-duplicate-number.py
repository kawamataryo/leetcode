#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = set([])
        for n in nums:
            if n in nums_set:
                return n
            else:
                nums_set.add(n)
# @lc code=end
