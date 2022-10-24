#
# @lc app=leetcode id=1816 lang=python3
#
# [1816] Truncate Sentence
#

# @lc code=start
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        space_count = 0
        for i in range(len(s)):
            if s[i] == " ":
                space_count += 1
            if space_count > k - 1:
                return s[:i]
        return s
# @lc code=end
