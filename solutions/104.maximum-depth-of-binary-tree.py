#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def traverse_node(node: TreeNode, depth: int) -> int:
            depth += 1
            if node.right is None and node.left is None:
                return depth
            if node.left is not None and node.right is not None:
                return max(traverse_node(node.left, depth), traverse_node(node.right, depth))
            if node.right is not None:
                return traverse_node(node.right, depth)
            if node.left is not None:
                return traverse_node(node.left, depth)
        return traverse_node(root, 0)
# @lc code=end
