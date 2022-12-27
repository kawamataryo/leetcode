#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # root_to_leafが不明
        root_to_leaf = 0
        stack = [(root, 0)]

        while stack:
            node, curr_number = stack.pop()
            if node is not None:
                curr_number = (curr_number << 1) | node.val
                if node.left is None and node.right is None:
                    root_to_leaf += curr_number
                else:
                    stack.append((node.right, curr_number))
                    stack.append((node.left, curr_number))
        return root_to_leaf
# @lc code=end
