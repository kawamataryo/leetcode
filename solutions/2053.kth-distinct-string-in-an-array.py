#
# @lc app=leetcode id=2053 lang=python3
#
# [2053] Kth Distinct String in an Array
#

# @lc code=start
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_map = {}
        for s in arr:
            if s in count_map:
                count_map[s] += 1
            else:
                count_map[s] = 1

        distinct_count = 0
        for s in arr:
            if count_map[s] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return s
        return ""
# @lc code=end
