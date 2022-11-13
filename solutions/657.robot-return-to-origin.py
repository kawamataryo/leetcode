#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_pair_dict = {
            "U": "D",
            "D": "U",
            "L": "R",
            "R": "L"
        }
        move_set = set()
        for move in moves:
            if move in move_set:
                move_set.remove(move)
            else:
                move_set.add(move_pair_dict[move])
        return len(move_set) == 0
# @lc code=end
