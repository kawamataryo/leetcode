#
# @lc app=leetcode id=1812 lang=python3
#
# [1812] Determine Color of a Chessboard Square
#

# @lc code=start
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        horizontal = {
            "a": False,
            "b": True,
            "c": False,
            "d": True,
            "e": False,
            "f": True,
            "g": False,
            "h": True,
        }

        return horizontal[coordinates[0]] != int(coordinates[1]) % 2 == 0
# @lc code=end
