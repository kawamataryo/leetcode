#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        values = []
        def collectValue(node: Optional[TreeNode]):
            if node is None:
                return
            values.append(node.val)
            collectValue(node.left)
            collectValue(node.right)
        collectValue(root)

        values.sort()

        result = TreeNode(values[0])
        currentNode = result

        for val in values[1:]:
            currentNode.right = TreeNode(val)
            currentNode = currentNode.right

        return result

# @lc code=end
