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
  if(!list1) {
    return list2
  }
  if(!list2) {
    return list1
  }

  const listNodeToList = (node: ListNode): number[] => {
    const _listNodeToList = (node: ListNode | null, result: number[]): number[] => {
      if (!node) {
        return result
      }

      return _listNodeToList(node, [...result, node.val])
    }

    return _listNodeToList(node, [])
  }

  const listToNodeList = (list: number[]) => {
    const _listToNodeList = (list: number[], node: ListNode | null) => {
      if(list.length === 0) {
        return node
      }

      if(!node) {
        node = new ListNode(list[0])
      } else {
        node.val = list[0]
      }

      if (list.length === 1) {
        node.next = null
      } else {
        node.next = new ListNode()
      }

      return _listToNodeList(list.slice(1), node.next)
    }
    const firstNode = new ListNode()
    _listToNodeList(list, firstNode)

    return firstNode
  }



  return listToNodeList([...listNodeToList(list1), ...listNodeToList(list2)].sort())
};
// @lc code=end
