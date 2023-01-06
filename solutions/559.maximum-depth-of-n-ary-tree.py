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
        max_depth_children = 0
        for child in root.children:
            depth = self.maxDepth(child)
            max_depth_children = max(max_depth_children, depth)
        return max_depth_children + 1
# @lc code=end
