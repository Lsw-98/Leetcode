/*
 * function ListNode(x){
 *   this.val = x;
 *   this.next = null;
 * }
 */

/**
 * 
 * @param head ListNode类 
 * @return bool布尔型
 */
function hasCycle(head) {
  let set = new WeakSet();
  let p = head;
  while (p !== null) {
    if (set.has(p)) {
      return true;
    } else {
      set.add(p)
    }
    p = p.next;
  }
  return false;
}
module.exports = {
  hasCycle: hasCycle
};