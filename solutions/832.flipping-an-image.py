#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            for i in range(math.ceil(len(row) / 2)):
                tmp = row[i]
                row[i] = row[-i-1] ^ 1
                row[-i-1] = tmp ^ i

        return image
# @lc code=end
