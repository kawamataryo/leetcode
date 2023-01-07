#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
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
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        x_condition = None
        y_condition = None

        q = deque([(root, 0, None)])
        while q:
            node, depth, parent_val = q.popleft()
            if node.val == x:
                x_condition = [depth, parent_val]
                continue
            if node.val == y:
                y_condition = [depth, parent_val]
                continue
            if node.left is not None:
                q.append((node.left, depth + 1, node.val))
            if node.right is not None:
                q.append((node.right, depth + 1, node.val))

        if x_condition is not None and y_condition is not None:
            return x_condition[0] == y_condition[0] and x_condition[1] != y_condition[1]
        else:
            return False

# @lc code=end
