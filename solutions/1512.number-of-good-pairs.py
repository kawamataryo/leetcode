#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pair_count = 0
        for x in range(len(nums)):
            for y in range (x + 1, len(nums)):
                if(nums[x] == nums[y]):
                    good_pair_count+= 1

        return good_pair_count

# @lc code=end
