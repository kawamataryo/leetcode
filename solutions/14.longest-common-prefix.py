#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ziped_strs = zip(*[list(s) for s in strs])

        output = ''
        for strs in ziped_strs:
            standard_val = strs[0]
            if all([s == standard_val for s in strs]):
                output += standard_val
            else:
                break
        return output

        # 参考メモ
        # [all()とany()は意外と使える子かもしれない。 - podhmoの日記](https://podhmo.hatenadiary.org/entry/20111213/1323788999)

# @lc code=end
