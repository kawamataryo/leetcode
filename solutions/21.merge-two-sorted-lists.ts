/*
 * @lc app=leetcode id=21 lang=typescript
 *
 * [21] Merge Two Sorted Lists
 */

// @lc code=start
/**
 */
 class ListNode {
     val: number
     next: ListNode | null
     constructor(val?: number, next?: ListNode | null) {
         this.val = (val===undefined ? 0 : val)
         this.next = (next===undefined ? null : next)
     }
 }

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  const listNodeToList = (node: ListNode | null, result: number[]): number[] => {
    if (!node) {
      return result
    }

    return listNodeToList(node, [...result, node.val])
  }

  if(!list1) {
    return list2
  }
  if(!list2) {
    return list1
  }
};
// @lc code=end
