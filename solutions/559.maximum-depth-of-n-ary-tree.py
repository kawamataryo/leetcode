#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        def traversal_node(node: 'Node', depth):
            if node.children is None:
                return depth
            return [traversal_node(child_node, depth + 1) for child_node in node.children]

        depths = traversal_node(root, 1)
        return max(depths)
# @lc code=end
