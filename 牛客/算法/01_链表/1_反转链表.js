/*function ListNode(x){
    this.val = x;
    this.next = null;
}*/
function ReverseList(pHead) {
  let cur = pHead
  let pre = null

  while (cur) {
    let temp = cur.next
    cur.next = pre
    pre = cur
    cur = temp
  }
  return pre
}
module.exports = {
  ReverseList: ReverseList
};