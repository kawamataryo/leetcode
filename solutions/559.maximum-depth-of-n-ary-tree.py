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

        q = deque([(root, 1)])
        max_depth = 0

        while q:
            node, depth = q.popleft()
            if depth > max_depth:
                max_depth = depth
            for child in node.children:
                q.append((child, depth + 1))
        return max_depth
# @lc code=end
