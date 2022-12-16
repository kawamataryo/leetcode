#
# @lc app=leetcode id=2331 lang=python3
#
# [2331] Evaluate Boolean Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        stack = queue.deque([root])

        while stack:
            node = stack.pop()
            if node.left and node.right:
                if node.left.val <= 1 and node.right.val <= 1:
                    if node.val == 2:
                        node.val = node.left.val or node.right.val
                    else:
                        node.val = node.left.val and node.right.val
                else:
                    stack.append(node)
                    stack.append(node.left)
                    stack.append(node.right)
            else:
                continue
        return node.val == 1
    # @lc code=end
