#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_paths = 0

        def visit(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left = visit(node.left)
            right = visit(node.right)
            self.max_paths = max(self.max_paths, left + right)

            return 1 + max(left, right)

        visit(root)

        return self.max_paths

# @lc code=end
