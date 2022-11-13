#
# @lc app=leetcode id=2351 lang=python3
#
# [2351] First Letter to Appear Twice
#

# @lc code=start
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letter_set = set()
        for i in range(len(s)):
            if s[i] in letter_set:
                return s[i]
            else:
                letter_set.add(s[i])
# @lc code=end
