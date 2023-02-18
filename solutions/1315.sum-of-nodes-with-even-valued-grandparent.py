#
# @lc app=leetcode id=1315 lang=python3
#
# [1315] Sum of Nodes with Even-Valued Grandparent
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = []
        def traverse(node, parents):
            if node is None:
                return 0
            gp_num = parents[0]
            if gp_num % 2 == 0:
                ans.append(node.val)
            traverse(node.left, parents[1:] + [node.val])
            traverse(node.right, parents[1:] + [node.val])

        traverse(root, [1,1])

        return sum(ans)



# @lc code=end
