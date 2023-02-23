#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")]+=1
            t = tuple(count)
            if t in h_map:
                h_map[t].append(s)
            else:
                h_map[t] = [s]

        return h_map.values()
# @lc code=end
