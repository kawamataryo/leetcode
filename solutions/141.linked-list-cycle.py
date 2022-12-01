#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        current_node = head

        while current_node not in visited_nodes and current_node is not None:
            visited_nodes.add(current_node)
            current_node = current_node.next
        return current_node is not None
# @lc code=end
