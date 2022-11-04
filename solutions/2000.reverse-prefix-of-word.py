#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)

        if index < 0:
            return word

        prefix, rest = word[:index+1], word[index+1:]
        return prefix[::-1] + rest
# @lc code=end
