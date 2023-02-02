#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_arr = []
        i = 0
        counter = 1
        max_i = len(arr)
        while len(missing_arr) < k:
            if i < max_i and counter >= arr[i]:
                i += 1
                counter += 1
            else:
                missing_arr.append(counter)
                counter += 1
        return missing_arr[-1]



# @lc code=end
