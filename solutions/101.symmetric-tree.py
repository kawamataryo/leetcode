#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        q = deque([(root.left, False), (root.right, True)])

        left_values = []
        right_values = []

        while q:
            node, is_right = q.popleft()
            if is_right:
                if node is not None:
                    right_values.append(node.val)
                    q.append((node.right, True))
                    q.append((node.left, True))
                else:
                    right_values.append(None)
            else:
                if node is not None:
                    left_values.append(node.val)
                    q.append((node.left, False))
                    q.append((node.right, False))
                else:
                    left_values.append(None)

        return left_values == right_values


# @lc code=end
