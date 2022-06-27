/*
 * function ListNode(x){
 *   this.val = x;
 *   this.next = null;
 * }
 */

/**
  * 
  * @param head ListNode类 
  * @param n int整型 
  * @return ListNode类
  */
function removeNthFromEnd(head, n) {
  let fast = head, slow = head;
  for (let i = 0; i < n; i++)  fast = fast.next;
  if (fast == null) return head.next;

  let pre;

  while (fast != null) {
    fast = fast.next;
    pre = slow;
    slow = slow.next;
  }

  pre.next = slow.next;
  return head;
}
module.exports = {
  removeNthFromEnd: removeNthFromEnd
};