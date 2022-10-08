#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # case 1 greedy
        # --------------------
        # numsLength = len(nums)
        # for x in range(numsLength):
        #     for y in range(x + 1, numsLength):
        #         if target - nums[x] == nums[y]:
        #             return [x, y]

        # case 2 two-path hashmap
        # --------------------
        # hashmap = {}
        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashmap and hashmap[complement] != i:
        #         return [i, hashmap[complement]]

        # case 3 list
        # --------------------
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums:
                cIndex = nums.index(complement)
                if i != cIndex:
                    return [i, cIndex]

        # case 4 one-path hashmap
        # --------------------
        # hashmap = {}
        # for x in range(len(nums)):
        #     complement = target - nums[x]
        #     if complement in hashmap:
        #         return [x, hashmap[complement]]
        #     hashmap[nums[x]] = x


# @lc code=end
