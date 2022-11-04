#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start
import re

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        vowels_count = 0

        pointer_1 = 0
        pointer_2 = len(s) - 1
        while pointer_1 < pointer_2:
            if s[pointer_1] in vowels_set:
                vowels_count+=1
            if s[pointer_2] in vowels_set:
                vowels_count-=1
            pointer_1+=1
            pointer_2-=1

        return vowels_count == 0
# @lc code=end
