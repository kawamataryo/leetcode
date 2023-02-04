#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left = 1
        right = num // 2

        while left <= right:
            mid = (left + right) // 2
            multiple = mid ** 2
            if multiple == num:
                return True
            if multiple < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
# @lc code=end
