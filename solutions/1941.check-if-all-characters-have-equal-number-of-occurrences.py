#
# @lc app=leetcode id=1941 lang=python3
#
# [1941] Check if All Characters Have Equal Number of Occurrences
#

# @lc code=start
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char_dict = {}
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        base_val = char_dict[s[0]]
        for key in char_dict:
            if base_val != char_dict[key]:
                return False
        return True
# @lc code=end
