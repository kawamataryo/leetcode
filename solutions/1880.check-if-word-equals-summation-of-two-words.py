#
# @lc app=leetcode id=1880 lang=python3
#
# [1880] Check if Word Equals Summation of Two Words
#

# @lc code=start
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def encode(s):
            return int("".join([str(ord(char) - 97) for char in s]))
        return encode(firstWord) + encode(secondWord) == encode(targetWord)
# @lc code=end
