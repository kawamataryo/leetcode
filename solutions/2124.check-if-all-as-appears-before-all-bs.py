#
# @lc app=leetcode id=2124 lang=python3
#
# [2124] Check if All A's Appears Before All B's
#

# @lc code=start
class Solution:
    def checkString(self, s: str) -> bool:
        appeared_b = False
        for i in range(len(s)):
            if s[i] == 'b':
                appeared_b = True
            elif appeared_b:
                return False
        return True
# @lc code=end
