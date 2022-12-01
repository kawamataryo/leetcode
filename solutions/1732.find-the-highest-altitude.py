#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitudes = 0
        highest_altitude = 0
        for g in gain:
            current_altitudes = current_altitudes + g
            if current_altitudes > highest_altitude:
                highest_altitude = current_altitudes
        return highest_altitude
# @lc code=end
