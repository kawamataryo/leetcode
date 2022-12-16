#
# @lc app=leetcode id=1935 lang=python3
#
# [1935] Maximum Number of Words You Can Type
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = [set(word) for word in text.split()]
        count = 0
        for word in words:
            count += 1
            for letter in brokenLetters:
                if letter in word:
                    count -= 1
                    break
        return count
# @lc code=end
