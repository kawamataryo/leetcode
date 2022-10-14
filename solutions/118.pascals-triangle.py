#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            if i == 1:
                result.append([1, 1])
                continue

            inner_array = []
            prev_array = result[i - 1]
            for x in range(1, len(prev_array)):
                inner_array.append(prev_array[x] + prev_array[x - 1])
            result.append([1] + inner_array + [1])

        return result
# @lc code=end
