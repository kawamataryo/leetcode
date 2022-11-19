#
# @lc app=leetcode id=1725 lang=python3
#
# [1725] Number Of Rectangles That Can Form The Largest Square
#

# @lc code=start
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_length = 0
        count = 0

        for rectangle in rectangles:
            square_length = rectangle[0] if rectangle[0] < rectangle[1] else rectangle[1]
            if square_length > max_length:
                max_length = square_length
                count = 1
            elif square_length== max_length:
                count += 1
        return count
# @lc code=end
