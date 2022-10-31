#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
import math

class Solution:
    def reverseWords(self, s: str) -> str:
        s_length = len(s)

        i, w_i = 0, 0
        while i < s_length:
            if s[i] == " ":
                for x in range(math.floor(w_i / 2)):
                    # replace char
                    tmp = s[i - 1 - w_i + x]
                    s[i - 1 - w_i + x] = s[i - 1 - x]
                    s[i - 1 -x] = tmp
                w_i = 0
            else:
                w_i += 1
            i += 1

        return s
# @lc code=end
