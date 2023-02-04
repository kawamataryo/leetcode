#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = 0
        t_i = 0
        s_len = len(s)
        t_len = len(t)

        while s_i < s_len and t_i < t_len:
            if s[s_i] == t[t_i]:
                s_i += 1
            t_i += 1
        return True if s_i == s_len else False

# @lc code=end
