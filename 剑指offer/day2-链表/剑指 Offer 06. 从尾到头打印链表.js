/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {number[]}
 */
var reversePrint = function (head) {
  const res = []
  let pre = null
  while (head) {
    const temp = head.next
    head.next = pre
    pre = head
    head = temp
  }

  // 先反转链表，再取数
  while (pre) {
    res.push(pre.val)
    pre = pre.next
  }
  return res
};