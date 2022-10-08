#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # list nodeから配列に変える
        # list nodeに戻す
        if(not l1 and not l2):
            return None
        if(not l1 or not l2):
            return l1 or l2

        sorted_list = sorted(self.to_list(l1) + self.to_list(l2))
        return self.to_list_node(sorted_list)

    def to_list(self, node: ListNode):
        if(node.next is None):
            return [node.val]
        return [node.val] + self.to_list(node.next)

    def to_list_node(self, li):
        if(not li):
            return None
        return ListNode(li.pop(0), self.to_list_node(li))
# @lc code=end
