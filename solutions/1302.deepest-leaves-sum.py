#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import namedtuple

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepest = [0, 0]
        def dfs(node: Optional[TreeNode], level: int):
            if node is None:
                return
            if node.left is None and node.right is None:
                if level > deepest[0]:
                    deepest[0] = level
                    deepest[1] = node.val
                    return
                if level == deepest[0]:
                    deepest[1] += node.val
                    return
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return deepest[1]
# @lc code=end
