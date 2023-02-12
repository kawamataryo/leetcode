#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = deque([])
        reverse_values = deque([])
        while head:
            values.append(head.val)
            reverse_values.appendleft(head.val)
            head = head.next

        return values == reverse_values
# @lc code=end
