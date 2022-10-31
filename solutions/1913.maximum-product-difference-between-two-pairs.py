#
# @lc app=leetcode id=1913 lang=python3
#
# [1913] Maximum Product Difference Between Two Pairs
#

# @lc code=start
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        mx1, mx2 = 0, 0
        mi1, mi2 = 100000, 100000

        for n in nums:
            if n <= mi1:
                mi1, mi2, = n, mi1
            elif n < mi2:
                mi2 = n
            if n >= mx1:
                mx1, mx2 = n, mx1
            elif n > mx2:
                mx2 = n

        return mx1 * mx2 - mi1 * mi2

# @lc code=end
