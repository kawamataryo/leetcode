#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs:
            while len(prefix) > 0:
                if prefix == s[:len(prefix)]:
                    break
                prefix = prefix[:-1]
            if len(prefix) == 0:
                break

        return prefix
# @lc code=end
