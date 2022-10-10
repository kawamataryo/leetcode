#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2 != 0):
            return False

        pair = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = []

        for char in s:
            if char in pair:
                stack.append(pair[char])
            elif len(stack) > 0 and stack[-1] == char:
                stack.pop()
            else:
                return False
        return len(stack) == 0
# @lc code=end
