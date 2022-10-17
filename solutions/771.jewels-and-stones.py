#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
import re

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len(re.findall(f'[{jewels}]', stones))
# @lc code=end
