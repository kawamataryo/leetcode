#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] + [0] * n

        # n = n if n <= 2
        # n = n(n-1) + n(n-2) if n > 2
        for i in range(1, n + 1):
            dp[i] += dp[i - 1] if i >= 1 else 0
            dp[i] += dp[i - 2] if i >= 2 else 0

        return dp[n]
# @lc code=end
