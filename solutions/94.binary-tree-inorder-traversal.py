#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = deque([])
        current = root
        output = []
        while True:
            if current is None:
                if stack:
                    node = stack.pop()
                    output.append(node.val)
                    current = node.right
                else:
                    break
            else:
                stack.append(current)
                current = current.left
        return output
# @lc code=end
