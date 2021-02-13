#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map_single = {
            'I':  1,
            'V':  5,
            'X':  10,
            'L':  50,
            'C':  100,
            'D':  500,
            'M':  1000
        }
        roman_map_double = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

        double_count = 0
        for word, value in roman_map_double.items():
            if word in s:
                double_count += value
                s = s.replace(word, '')

        single_count = sum([roman_map_single[x] for x in s])
        return single_count + double_count

        # 'MCM'.strip('CM')が''になるのはなぜ？
        # stripは含まれるものが削除される。文字順は考慮しない。

# @lc code=end
