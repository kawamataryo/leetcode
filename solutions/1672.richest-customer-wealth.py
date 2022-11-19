#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
import functools

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            # replaceable sum()
            wealth = functools.reduce(lambda a, b: a+b, account)
            # replaceable max()
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth
# @lc code=end
