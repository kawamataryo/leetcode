#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x):
        s = 1 if x >= 0 else -1
        r = int(f"{s*x}"[::-1])
        return s*r if r < 2**31 else 0

# @lc code=end
