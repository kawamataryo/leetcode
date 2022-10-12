#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        while i < len(nums) and nums[i - 1] <= nums[i]:
            if nums[i - 1] == nums[i]:
                duplicated_num = nums.pop(i)
                nums.append(duplicated_num - 1)
            else:
                i+=1

        return i

# @lc code=end
