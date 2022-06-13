/*function ListNode(x){
    this.val = x;
    this.next = null;
}*/
function Merge(pHead1, pHead2) {
  if (!pHead1) return pHead2;
  if (!pHead2) return pHead1;
  
  if (pHead1.val <= pHead2.val) {
    pHead1.next = Merge(pHead1.next, pHead2);
    return pHead1
  } else {
    pHead2.next = Merge(pHead2.next, pHead1);
    return pHead2
  }
}
module.exports = {
  Merge: Merge
};