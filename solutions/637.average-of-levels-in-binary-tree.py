#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        q = deque([(root, 0)])
        current_depth = 0
        current_depth_values = []
        result = []
        while q:
            node, depth = q.popleft()
            if current_depth == depth:
                current_depth_values.append(node.val)
            else:
                result.append(sum(current_depth_values) / len(current_depth_values))
                current_depth_values = []
                current_depth = depth
                current_depth_values.append(node.val)

            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

        result.append(sum(current_depth_values) / len(current_depth_values))

        return result
# @lc code=end
