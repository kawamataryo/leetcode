#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = None
        node = None
        while head:
            if head.val == val:
                head = head.next
                if node:
                    node.next = None
                continue
            if ans is None:
                node = head
                ans = node
            else:
                node.next = head
                node = head
            head = head.next
        return ans


# @lc code=end
