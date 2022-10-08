#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not needle in haystack:
            return -1
        return haystack.find(needle)
        # scanしてなければ -1
        # needleが空有白の場合は 0
# @lc code=end
