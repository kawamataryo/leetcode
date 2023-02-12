#
# @lc app=leetcode id=1481 lang=python3
#
# [1481] Least Number of Unique Integers after K Removals
#

# @lc code=start
import collections

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        nums_dict = collections.Counter(arr)
        nums_amount = sorted(list(nums_dict.values()))

        index = 0
        for _ in range(k):
            nums_amount[index] -= 1
            if nums_amount[index] == 0:
                index = index + 1

        return len([num for num in nums_amount if num != 0])
# @lc code=end
