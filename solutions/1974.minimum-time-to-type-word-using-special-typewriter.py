#
# @lc app=leetcode id=1974 lang=python3
#
# [1974] Minimum Time to Type Word Using Special Typewriter
#

# @lc code=start
class Solution:
    def minTimeToType(self, word: str) -> int:
        seconds = 0
        current_char = 'a'
        for char in word:
            distance = abs(ord(current_char) - ord(char))
            seconds += min(distance, abs(distance - 26))
            current_char = char
            seconds+=1
        return seconds
# @lc code=end
