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
  let cur = head
  while (cur) {
    const temp = cur.next
    cur.next = pre
    pre = cur
    cur = temp
  }
  while (pre) {
    res.push(pre.val)
    pre = pre.next
  }
  return res
};