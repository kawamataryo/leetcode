#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0
        for i in range(1,len(points)):
            seconds += max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]))
        return seconds
# @lc code=end
