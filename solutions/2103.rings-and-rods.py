#
# @lc app=leetcode id=2103 lang=python3
#
# [2103] Rings and Rods
#

# @lc code=start
class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for _ in range(10)]

        i = 0
        while i < len(rings):
            rods[int(rings[i + 1])].add(rings[i])
            i+=2

        return len(["ok" for rod in rods if len(rod) > 2])

# @lc code=end
