#
# @lc app=leetcode id=2006 lang=python3
#
# [2006] Count Number of Pairs With Absolute Difference K
#

# @lc code=start
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hash_map = {}
        for n in nums:
            if n in hash_map:
                hash_map[n] += 1
            else:
                hash_map[n] = 1

        result = 0
        for n in nums:
            target_num = n + k
            if target_num in hash_map:
                result += hash_map[target_num]

        return result
# @lc code=end
