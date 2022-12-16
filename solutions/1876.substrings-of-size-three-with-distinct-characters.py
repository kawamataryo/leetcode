#
# @lc app=leetcode id=1876 lang=python3
#
# [1876] Substrings of Size Three with Distinct Characters
#

# @lc code=start
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        substrings = [s[i:i+3]for i in range(len(s) - 2)]
        good_substrings = [substring for substring in substrings if len(set(substring)) == 3]
        return len(good_substrings)
# @lc code=end
