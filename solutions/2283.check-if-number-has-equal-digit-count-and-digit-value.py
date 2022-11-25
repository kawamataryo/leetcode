#
# @lc app=leetcode id=2283 lang=python3
#
# [2283] Check if Number Has Equal Digit Count and Digit Value
#

# @lc code=start
class Solution:
    def digitCount(self, num: str) -> bool:
        digit_count_dict = {}
        for n in num:
            if n in digit_count_dict:
                digit_count_dict[n] += 1
            else:
                digit_count_dict[n] = 1

        for i in range(len(num)):
            if str(i) not in digit_count_dict:
                if num[i] == '0':
                    continue
                else:
                    return False
            if digit_count_dict[str(i)] == int(num[i]):
                continue
            return False
        return True
# @lc code=end
