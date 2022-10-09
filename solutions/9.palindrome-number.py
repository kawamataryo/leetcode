#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        stringX = str(x)
        length = len(stringX)
        halfLength = math.floor(length / 2)

        if length % 2 == 0:
            return stringX[0:halfLength] == stringX[halfLength::][::-1]
        else:
            return stringX[0:halfLength] == stringX[halfLength + 1::][::-1]
# @lc code=end
