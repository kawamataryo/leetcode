#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#

# @lc code=start
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_name_map = {}
        for i in range(len(names)):
            height_name_map[heights[i]] = names[i]

        sorted_height_name_list = sorted(height_name_map.items(), reverse=True)

        return [v[1] for v in sorted_height_name_list]
# @lc code=end
