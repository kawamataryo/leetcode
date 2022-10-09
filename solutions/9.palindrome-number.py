#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # first
        # ------------------------
        # if x < 0:
        #     return False
        # stringX = str(x)
        # length = len(stringX)
        # halfLength = math.floor(length / 2)

        # if length % 2 == 0:
        #     return stringX[0:halfLength] == stringX[halfLength::][::-1]
        # else:
        #     return stringX[0:halfLength] == stringX[halfLength + 1::][::-1]

        # popular solution
        # ------------------------
        # if x < 0:
        #     return False

        # return str(x) == str(x)[::-1]

        # best solution
        # ------------------------
        if x < 0 or (x > 0 and x%10 == 0):
            return False
        result = 0
        while x > result:
            result = result * 10 + x % 10
            x = x // 10
        return True if (x == result or x == result // 10) else False

# @lc code=end
