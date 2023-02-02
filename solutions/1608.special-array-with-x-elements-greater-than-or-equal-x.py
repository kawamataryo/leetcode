#
# @lc app=leetcode id=1608 lang=python3
#
# [1608] Special Array With X Elements Greater Than or Equal X
#

# @lc code=start
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        for i in range(len(nums) + 1):
            count = 0
            for num in sorted_nums:
                print(f'i: {i}')
                print(f'num: {num}')
                if i <= num:
                    count += 1
                else:
                    break
            if i == count:
                return i
        return -1
# @lc code=end
