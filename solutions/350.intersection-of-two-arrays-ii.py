#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
import collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counter = collections.Counter(nums1)
        nums2_counter = collections.Counter(nums2)
        nums_intersection = set(nums1) & set(nums2)

        ans = []
        for num in nums_intersection:
            for _i in range(min(nums1_counter[num], nums2_counter[num])):
                ans.append(num)

        return ans


# @lc code=end
