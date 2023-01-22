#
# @lc app=leetcode id=888 lang=python3
#
# [888] Fair Candy Swap
#

# @lc code=start
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        bobSizes_set = set(bobSizes)

        for num in aliceSizes:
            swap_num = num - diff
            if swap_num in bobSizes_set:
                return [num, swap_num]
# @lc code=end
