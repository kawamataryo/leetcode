#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     # 回文かどうか判定する
    #     if x < 0:
    #         return False
    #     if x == self._reverse_int(x):
    #         return True
    #     return False

    # def _reverse_int(self, x: int) -> int:
    #     return int(''.join(list(str(x))[::-1]))

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0 and x != 0:
            return False

        revertNumber = 0
        while x > revertNumber:
            revertNumber = revertNumber * 10 + x % 10
            x //= 10

        return x == revertNumber or x == revertNumber // 10
# @lc code=end
