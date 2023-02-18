#
# @lc app=leetcode id=2265 lang=python3
#
# [2265] Count Nodes Equal to Average of Subtree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = []

        def aggregate_subtree(node):
            if node is None:
                return [0, 0]
            left_total, left_count = aggregate_subtree(node.left)
            right_total, right_count = aggregate_subtree(node.right)

            total = left_total + right_total + node.val
            count = left_count + right_count + 1
            if node.val == total // count:
                ans.append(1)

            return [
                total,
                count
            ]

        aggregate_subtree(root)

        return len(ans)
# @lc code=end
