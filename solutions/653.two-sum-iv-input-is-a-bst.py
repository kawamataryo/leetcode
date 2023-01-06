#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def visit(node, values):
            if not node:
                return
            if node.left:
                visit(node.left, values)
            values.append(node.val)  # in-order traversal
            if node.right:
                visit(node.right, values)

        values = []
        visit(root, values)

        start, end = 0, len(values) - 1
        while start != end:
            total =  values[start] + values[end]
            if total == k:
                return True
            if total < k:
                start += 1
            else:
                end -= 1
        return False


# @lc code=end
