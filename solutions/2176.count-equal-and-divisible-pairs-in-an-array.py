#
# @lc app=leetcode id=2176 lang=python3
#
# [2176] Count Equal and Divisible Pairs in an Array
#

# @lc code=start
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pair = 0
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                for j in nums_dict[nums[i]]:
                    if i * j % k == 0:
                        pair+=1
                nums_dict[nums[i]].append(i)
            else:
                nums_dict[nums[i]] = [i]
        return pair
# @lc code=end
