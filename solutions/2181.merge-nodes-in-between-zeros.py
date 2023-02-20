#
# @lc app=leetcode id=2181 lang=python3
#
# [2181] Merge Nodes in Between Zeros
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans_nums = []
        while head:
            if head.val == 0:
                head = head.next
            total = 0
            while head is not None and head.val != 0:
                total += head.val
                head = head.next
            ans_nums.append(total)
            head = head.next

        ans_node = ListNode(ans_nums[0])
        ans_head = ans_node

        for val in ans_nums[1:]:
            node = ListNode(val)
            ans_head.next = node
            ans_head = node

        return ans_node
# @lc code=end
