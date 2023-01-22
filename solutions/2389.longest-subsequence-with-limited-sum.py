#
# @lc app=leetcode id=2389 lang=python3
#
# [2389] Longest Subsequence With Limited Sum
#

# @lc code=start
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        ans = []
        for query in queries:
            total = 0
            subsequence_count = 0
            for num in sorted_nums:
                total += num
                if query >= total:
                    subsequence_count += 1
                else:
                    break
            ans.append(subsequence_count)
        return ans
# @lc code=end
