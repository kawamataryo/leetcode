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

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        if not root.children:
            return [root.val]
        children = itertools.chain.from_iterable([self.postorder(node) for node in root.children])
        return [*children, root.val]
# @lc code=end
