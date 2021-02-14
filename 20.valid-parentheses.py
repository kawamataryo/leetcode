#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 最小単位としてペアがあるので、それを見つけてどんどん消していく方法
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()',"")
            s = s.replace('{}',"")
            s = s.replace('[]',"")
        return s == ''



# @lc code=end
