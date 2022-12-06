#
# @lc app=leetcode id=2206 lang=python3
#
# [2206] Divide Array Into Equal Pairs
#

# @lc code=start
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_dict = {}
        for n in nums:
            if n in nums_dict:
                nums_dict[n] += 1
            else:
                nums_dict[n] = 1

        for val in nums_dict.values():
            if val % 2 != 0:
                return False
        return True
# @lc code=end
