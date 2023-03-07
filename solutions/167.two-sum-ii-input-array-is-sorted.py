#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = 0
        l = len(numbers) - 1

        while f < l:
            s = numbers[f] + numbers[l]
            if s == target:
                return [f + 1, l + 1]
            if s < target:
                f += 1
            else:
                l -= 1
# @lc code=end
