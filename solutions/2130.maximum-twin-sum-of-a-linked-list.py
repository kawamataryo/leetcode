#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        return max([values[i] + values[-i-1] for i in range(len(values) // 2)])

# @lc code=end
