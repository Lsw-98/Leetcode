/*
 * function ListNode(x){
 *   this.val = x;
 *   this.next = null;
 * }
 */

/**
 * 
 * @param lists ListNode类一维数组 
 * @return ListNode类
 */
function mergeKLists(lists) {
  let arr = []

  for (let i = 0; i < lists.length; i++) {
    let p = lists[i]
    while (p !== null) {
      arr.push(p.val)
      p = p.next
    }
  }

  arr.sort((a, b) => a - b)

  let head = null
  let cur = null
  for (let j = 0; j < arr.length; j++) {
    let node = new ListNode(arr[j])
    if (head === null) {
      head = node
      cur = node
    } else {
      cur.next = node
      cur = node
    }
  }
  return head
}
module.exports = {
  mergeKLists: mergeKLists
};