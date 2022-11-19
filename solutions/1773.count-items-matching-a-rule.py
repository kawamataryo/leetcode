#
# @lc app=leetcode id=1773 lang=python3
#
# [1773] Count Items Matching a Rule
#

# @lc code=start
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key_index = {
            'type': 0,
            'color': 1,
            'name': 2
        }

        match_count = i = 0
        while i < len(items):
            if items[i][key_index[ruleKey]] == ruleValue:
                match_count += 1
            i+=1

        return match_count
# @lc code=end
