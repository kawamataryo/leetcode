#
# @lc app=leetcode id=2363 lang=python3
#
# [2363] Merge Similar Items
#

# @lc code=start
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        item_map = {}
        for item in [*items1, *items2]:
            if item[0] in item_map:
                item_map[item[0]] = [item_map[item[0]][0], item_map[item[0]][1] + item[1]]
            else:
                item_map[item[0]] = item

        return sorted(item_map.values(), key=lambda x: x[0])
# @lc code=end
