#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def sum_of_left(node: Optional[TreeNode], is_left: bool) -> int:
            if node is None:
                return 0
            if node.left is None and node.right is None:
                if is_left:
                    return node.val
                else:
                    return 0
            return sum_of_left(node.left, True) + sum_of_left(node.right, False)

        return sum_of_left(root, False)
# @lc code=end
