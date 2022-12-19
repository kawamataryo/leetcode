#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from itertools import chain

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        if root.children is None:
            return [root.val]

        childe_values = []
        for node in root.children:
            childe_values += self.preorder(node)

        return [root.val, *childe_values]
# @lc code=end
