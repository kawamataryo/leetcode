#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            an1 = -self._reverse_numbers(-x)
            if an1 < -2**31:
                return 0
            return an1
        an2 = self._reverse_numbers(x)
        if an2 > 2**31 - 1:
            return 0
        return an2

    def _reverse_numbers(self, x):
        return int(''.join(list(str(x))[::-1]))

# @lc code=end
