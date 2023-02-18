#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        values = deque([])

        def correct_value(node: TreeNode):
            values.append(node.val)

        def add_value(node: TreeNode):
            values.popleft()
            node.val += sum(values)

        def traverse_and_execute(node: Optional[TreeNode], func):
            if node is None:
                return
            traverse_and_execute(node.left, func)
            func(node)
            traverse_and_execute(node.right, func)

        traverse_and_execute(root, correct_value)
        traverse_and_execute(root, add_value)

        return root


# @lc code=end
