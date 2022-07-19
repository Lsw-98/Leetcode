/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var deleteNode = function (head, val) {
  if (head.val === val) return head.next
  let res = head
  let cur = head
  let pre = head
  while (cur) {
    if (cur.val === val) {
      if (cur.next !== null) {
        pre.next = cur.next
      } else {
        pre.next = null
      }
      break
    } else {
      pre = cur
      cur = cur.next
    }
  }
  return res
};