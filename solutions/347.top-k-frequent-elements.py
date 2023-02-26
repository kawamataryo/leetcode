#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq_heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(freq_heap)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(freq_heap)[1])

        return ans
# @lc code=end
