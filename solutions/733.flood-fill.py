#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        q = deque([(sr, sc)])
        while q:
            r, c = q.popleft()
            old_color, image[r][c] = image[r][c], color

            if old_color == color:
                continue
            if r < len(image) - 1 and image[r + 1][c] == old_color:
                q.append((r + 1, c))
            if r > 0 and image[r - 1][c] == old_color:
                q.append((r - 1, c))
            if c < len(image[0]) - 1 and image[r][c + 1] == old_color:
                q.append((r, c + 1))
            if c > 0 and image[r][c - 1] == old_color:
                q.append((r, c - 1))
        return image

# @lc code=end
