#
# @lc app=leetcode id=2022 lang=python3
#
# [2022] Convert 1D Array Into 2D Array
#

# @lc code=start
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        original_que = deque(original)
        for row in range(m):
            ans_col = []
            for col in range(n):
                if len(original_que) == 0:
                    return []
                num = original_que.popleft()
                ans_col.append(num)
            ans.append(ans_col)

        if len(original_que) == 0:
            return ans
        else:
            return []
# @lc code=end
