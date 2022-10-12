/*
 * @lc app=leetcode id=21 lang=typescript
 *
 * [21] Merge Two Sorted Lists
 */

// @lc code=start
/**
 */
//  class ListNode {
//      val: number
//      next: ListNode | null
//      constructor(val?: number, next?: ListNode | null) {
//          this.val = (val===undefined ? 0 : val)
//          this.next = (next===undefined ? null : next)
//      }
//  }

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  if(!list1) {
    return list2
  }
  if(!list2) {
    return list1
  }

  const toList = (node: ListNode): number[] => {
    if (!node.next) {
      return [node.val]
    }
    return [node.val, ...toList(node.next)]
  }

  const toNodeList = (list: number[]) => {
    if(!list) {
        return null
    }
    return new ListNode(list[0], toNodeList(list.slice(1)))
  }


  return toNodeList([...toList(list1), ...toList(list2)].sort())
};
// @lc code=end
