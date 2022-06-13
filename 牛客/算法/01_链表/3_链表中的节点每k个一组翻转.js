/*
 * function ListNode(x){
 *   this.val = x;
 *   this.next = null;
 * }
 */

/**
  * 
  * @param head ListNode类 
  * @param k int整型 
  * @return ListNode类
  */
function reverseKGroup(head, k) {
  let cur = head
  let pre = null
  let node = head

  for (let i = 0; i < k; i++) {
    if (node === null) {
      return head
    }
    node = node.next
  }

  for (let i = 0; i < k; i++) {
    let temp = cur.next
    cur.next = pre
    pre = cur
    cur = temp
  }

  head.next = reverseKGroup(cur, k)
  return pre
}
module.exports = {
  reverseKGroup: reverseKGroup
};