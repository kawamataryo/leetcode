#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # correct_count = 0
        # for i in range(len(nums)):
        #     if nums[correct_count] != val:
        #         correct_count+=1
        #     else:
        #         removed_val = nums.pop(correct_count)
        #         nums.append(removed_val)

        # return correct_count

        while val in nums:
            nums.remove(val)

        return len(nums)

# @lc code=end
