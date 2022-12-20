#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
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
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        if not root.children:
            return [root.val]

        stack = collections.deque([root])
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)
            for n in node.children:
                stack.append(n)

        return result[::-1]
# @lc code=end
