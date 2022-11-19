#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        stuck = 0
        for char in s:
            if stuck == 0:
                count += 1
            if char == 'R':
                stuck += 1
            else:
                stuck -= 1
        return count
# @lc code=end
