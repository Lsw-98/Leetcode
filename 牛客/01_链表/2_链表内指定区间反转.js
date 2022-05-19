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
  const vHead = head
  let cur = vHead

  for (let i = 0; i < m - 1; i++) {
    cur = cur.next
  }

  let tempCur = cur
  let pre = null
  while ((n - m + 1)--) {
    let temp = tempCur.next
    tempCur.next = pre
    pre = tempCur
    tempCur = temp
  }

  cur.next = pre

  return vHead
}
module.exports = {
  reverseBetween: reverseBetween
};