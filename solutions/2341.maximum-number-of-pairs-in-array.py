#
# @lc app=leetcode id=2341 lang=python3
#
# [2341] Maximum Number of Pairs in Array
#

# @lc code=start
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        pair = rest = 0
        for val in nums_dict.values():
            q, r = divmod(val, 2)
            pair += q
            rest += r

        return [pair, rest]
# @lc code=end
