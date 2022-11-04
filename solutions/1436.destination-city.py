#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_city = set()
        maybe_destination_city = set()

        for i in range(len(paths)):
            if paths[i][0] in maybe_destination_city:
                maybe_destination_city.remove(paths[i][0])
            if paths[i][1] not in start_city:
                maybe_destination_city.add(paths[i][1])
            start_city.add(paths[i][0])

        return maybe_destination_city.pop()

# @lc code=end
