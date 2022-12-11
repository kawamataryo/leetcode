#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums_dict = {}
        for n in arr:
            if n in nums_dict:
                nums_dict[n] += 1
            else:
                nums_dict[n] = 1
        occurrences = nums_dict.values()
        return len(occurrences) == len(set(occurrences))
# @lc code=end
