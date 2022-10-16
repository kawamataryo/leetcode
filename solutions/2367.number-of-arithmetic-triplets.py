#
# @lc app=leetcode id=2367 lang=python3
#
# [2367] Number of Arithmetic Triplets
#

# @lc code=start
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        triplet_count = 0
        hash_table = {}

        for i in range(len(nums)):
            hash_table[nums[i]] = i

        for i in range(1, len(nums)):
            if nums[i] - diff in hash_table and nums[i] + diff in hash_table:
                triplet_count += 1

        return triplet_count




# @lc code=end
