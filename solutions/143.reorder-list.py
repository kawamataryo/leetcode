#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        reversed_list = None
        tmp_head = head

        values = []
        while tmp_head:
            values.append(tmp_head.val)
            tmp_head = tmp_head.next

        s = 0
        l = len(values) - 1
        while head:
            head.val = values[s]
            if head.next:
                head.next.val = values[l]
                head = head.next.next
            else:
                break
            s += 1
            l -= 1

# @lc code=end
