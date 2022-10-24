#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        oddLengths = []

        for x in range(len(arr)):
            if (x + 1) % 2 != 0:
                oddLengths.append(x)

            for y in oddLengths:
                result += sum(arr[x - y:x + 1])

        return result
# @lc code=end
