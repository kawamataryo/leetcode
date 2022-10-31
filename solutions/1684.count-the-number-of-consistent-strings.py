#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        allowed_set = set(allowed)

        for word in words:
            word_set = set(word)
            if allowed_set & word_set == word_set:
                result+=1

        return result
# @lc code=end
