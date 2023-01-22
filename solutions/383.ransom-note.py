#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        for char in magazine:
            if char in magazine_dict:
                magazine_dict[char] += 1
            else:
                magazine_dict[char] = 1

        for char in ransomNote:
            if char in magazine_dict and magazine_dict[char] > 0:
                magazine_dict[char] -= 1
            else:
                return False
        return True
# @lc code=end
