#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = {}, {}
        prefix_num, suffix_num = 1, 1
        length = len(nums)

        for i in range(length):
            prefix[i] = prefix_num
            suffix[length - i - 1] = suffix_num
            prefix_num *= nums[i]
            suffix_num *= nums[-i-1]

        ans = []
        for i in range(length):
            ans.append(prefix[i] * suffix[i])

        return ans
# @lc code=end
