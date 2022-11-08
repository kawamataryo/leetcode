#
# @lc app=leetcode id=2185 lang=python3
#
# [2185] Counting Words With a Given Prefix
#

# @lc code=start
import re
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        x = 0
        while x < len(words):
            if words[x][:len(pref)] == pref:
                count+=1
            x+=1

        return count


# @lc code=end
