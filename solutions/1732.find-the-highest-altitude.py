#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        max_gain = 0
        for i, g in enumerate(gain):
            altitude = altitudes[i] + g
            altitudes.append(altitude)
            if altitude > max_gain:
                max_gain = altitude
        return max_gain
# @lc code=end
