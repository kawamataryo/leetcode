#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # My first solution.
        # -------------------------
        # good_pair_count = 0
        # for x in range(len(nums)):
        #     for y in range (x + 1, len(nums)):
        #         if(nums[x] == nums[y]):
        #             good_pair_count+= 1
        # return good_pair_count

        # (WIP) My second solutions.
        # 15 min
        # -------------------------
        hash_table = {}
        for i in range(len(nums)):
            # FIXME: 同じ数が複数あることを考慮できていない
            hash_table[nums[i]] = i

        good_pair_count = 0
        for i in range(len(nums)):
            if nums[i] in hash_table and i < hash_table[nums[i]]:
                good_pair_count += 1

        return good_pair_count
# @lc code=end
