#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_num = int("0b" + a, base=2)
        b_num = int("0b" + b, base=2)

        return bin(a_num + b_num)[2:]
# @lc code=end