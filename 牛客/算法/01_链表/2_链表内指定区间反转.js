/*
 * function ListNode(x){
 *   this.val = x;
 *   this.next = null;
 * }
 */

/**
  * 
  * @param head ListNode类 
  * @param m int整型 
  * @param n int整型 
  * @return ListNode类
  */
function reverseBetween(head, m, n) {
  // 如果只有一个节点或m === n不需要翻转
  if (head === null || head.next === null || m === n) {
    return head
  }
  // start指向开始反转节点的前一个节点, 即 m - 1
  // end指向 n + 1
  let cur = head
  let start = null
  let end = null

  // 寻找start和end
  for (let i = 1; i <= n; i++) {
    if (i === m - 1) {
      start = cur
    }
    cur = cur.next
  }
  end = cur

  let pre = null
  let next = null
  // 如果起始节点不是头节点，说明start有值
  if (m > 1) {
    cur = start.next
    while (cur !== end) {
      next = cur.next
      cur.next = pre
      pre = cur
      cur = next
    }
    start.next.next = end
    start.next = pre
  } else { // 起始节点就是头节点，start没有值
    cur = head
    while (cur !== end) {
      next = cur.next
      cur.next = pre
      pre = cur
      cur = next
    }
    head.next = end
    head = pre
  }

  return head
}
module.exports = {
  reverseBetween: reverseBetween
};