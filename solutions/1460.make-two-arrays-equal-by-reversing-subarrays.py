#
# @lc app=leetcode id=1460 lang=python3
#
# [1460] Make Two Arrays Equal by Reversing Subarrays
#

# @lc code=start
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        nums_dict = {}
        for n in target:
            if n in nums_dict:
                nums_dict[n] += 1
            else:
                nums_dict[n] = 1
        for n in arr:
            if n in nums_dict:
                nums_dict[n] -= 1
            else:
                return False
        return len([v for v in nums_dict.values() if v != 0]) == 0
# @lc code=end
