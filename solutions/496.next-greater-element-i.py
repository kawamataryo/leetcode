#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_dict = {}
        for i in range(len(nums2)):
            for n in nums2[i+1:]:
                if n > nums2[i]:
                    greater_dict[nums2[i]] = n
                    break
            if nums2[i] not in greater_dict:
                    greater_dict[nums2[i]] = -1

        return [greater_dict[n] for n in nums1]
# @lc code=end
