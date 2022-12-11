#
# @lc app=leetcode id=2032 lang=python3
#
# [2032] Two Out of Three
#

# @lc code=start
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        set_3 = set(nums3)

        return list((set_1 & set_2) | (set_1 & set_3) | (set_2 & set_3))
# @lc code=end
