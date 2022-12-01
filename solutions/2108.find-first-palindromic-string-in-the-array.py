#
# @lc app=leetcode id=2108 lang=python3
#
# [2108] Find First Palindromic String in the Array
#

# @lc code=start
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindromic(word: str):
            i = 0
            while i < len(word) // 2:
                if word[i] != word[-(i+1)]:
                    return False
                i += 1
            return True

        for word in words:
            if is_palindromic(word):
                return word

        return ""
# @lc code=end
