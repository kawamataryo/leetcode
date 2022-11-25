#
# @lc app=leetcode id=2108 lang=python3
#
# [2108] Find First Palindromic String in the Array
#

# @lc code=start
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindromic(word: str):
            half = len(word) // 2
            if half < 1:
                return True
            return word[:half] == word[-half:][::-1]

        for word in words:
            if is_palindromic(word):
                return word

        return ""
# @lc code=end
