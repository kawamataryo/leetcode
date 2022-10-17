#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_table = {}
        good_pair_count = 0

        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]] = 1
            else:
                good_pair_count += hash_table[nums[i]]
                hash_table[nums[i]] += 1

        return good_pair_count
# @lc code=end
