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
from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([(root, 0)])
        max_depth = 0
        ans = 0
        while queue:
            node, depth = queue.popleft()
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
            if node.left is None and node.right is None:
                if depth == max_depth:
                    ans += node.val
                elif depth > max_depth:
                    max_depth = depth
                    ans = node.val
        return ans
# @lc code=end
