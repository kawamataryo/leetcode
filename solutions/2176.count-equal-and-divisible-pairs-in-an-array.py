#
# @lc app=leetcode id=2176 lang=python3
#
# [2176] Count Equal and Divisible Pairs in an Array
#

# @lc code=start
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pair = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    pair += 1

        return pair
# @lc code=end
