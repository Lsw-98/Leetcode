/*
 * function ListNode(x){
 *   this.val = x;
 *   this.next = null;
 * }
 */
/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param pHead ListNode类 
 * @param k int整型 
 * @return ListNode类
 */
function FindKthToTail(pHead, k) {
  let cur = pHead
  let pre = pHead

  for (let i = 0; i < k; i++) {
    if (cur) {
      cur = cur.next
      continue
    } else {
      return null
    }
  }

  while (cur) {
    cur = cur.next
    pre = pre.next
  }

  return pre
}
module.exports = {
  FindKthToTail: FindKthToTail
};