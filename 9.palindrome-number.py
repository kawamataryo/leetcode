#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 回分かどうか判定する
        if x < 0:
            return False
        if x == self._reverse_int(x):
            return True
        return False

    def _reverse_int(self, x: int) -> int:
        return int(''.join(list(str(x))[::-1]))
# @lc code=end
