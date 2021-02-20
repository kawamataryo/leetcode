#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splittedStr = s.strip().split(' ')
        convertLength = [len(x) for x in splittedStr]
        return convertLength[-1]
# @lc code=end
