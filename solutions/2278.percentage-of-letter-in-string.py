#
# @lc app=leetcode id=2278 lang=python3
#
# [2278] Percentage of Letter in String
#

# @lc code=start
import math
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        target_count = total_count = 0

        for char in s:
            if char == letter:
                target_count+=1
            total_count+=1
        return math.floor((target_count/total_count)*100)
# @lc code=end
