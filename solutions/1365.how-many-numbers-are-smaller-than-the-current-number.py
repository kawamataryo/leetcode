#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Greedy (My first solution)
        # ----------------------
        # result = [0] * len(nums)

        # for x in range(len(nums)):
        #     for y in range(len(nums)):
        #         if nums[x] != nums[y] and nums[x] > nums[y]:
        #             result[x] += 1

        # Hashmap
        # reference: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/solutions/819148/python-3-91-11-faster-52ms-time-explanation-added/
        # ----------------------
        length = len(nums)
        sorted_nums = sorted(nums)
        hash_map = {}

        for i in range(length):
            if sorted_nums[i] not in hash_map:
                hash_map[sorted_nums[i]] = i

        result = []
        for i in range(length):
            result.append(hash_map[nums[i]])

        return result
# @lc code=end
