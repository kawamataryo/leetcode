#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        result = 0
        while len(s) > 0:
            if s[0:2] in roman_map:
                result += roman_map[s[0:2]]
                s = s[2:]
            elif s[0:1] in roman_map:
                result += roman_map[s[0:1]]
                s = s[1:]

        return result
# @lc code=end
