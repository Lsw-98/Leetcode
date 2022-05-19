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
  let vHead = ListNode(0, head)
  let cur = vHead
  let pre = vHead

  for (let i = 0; i < n; i++) {
    if (cur && cur.next) {
      cur = cur.next
    } else {
      break
    }
  }

  while (cur && cur.next) {
    pre = pre.next
    cur = cur.next
  }

  pre.next = pre.next.next

  return vHead
}
module.exports = {
  removeNthFromEnd: removeNthFromEnd
};