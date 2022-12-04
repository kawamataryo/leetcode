#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        nodes = [root]
        while len(nodes) > 0:
            current_node = nodes[-1]

            if current_node is None:
                nodes.pop()
                continue
            if current_node.val >= low and current_node.val <= high:
                result += current_node.val
                nodes.pop()
            else:
                nodes.pop()

            if current_node.val < low:
                nodes.append(current_node.right)
            elif current_node.val > high:
                nodes.append(current_node.left)
            else:
                nodes.append(current_node.right)
                nodes.append(current_node.left)

        return result
# @lc code=end
