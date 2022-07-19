/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function (l1, l2) {
  const arr = []
  while (l1) {
    arr.push(l1.val)
    l1 = l1.next
  }
  while (l2) {
    arr.push(l2.val)
    l2 = l2.next
  }

  arr.sort((a, b) => { return a - b })
  let head = new TreeNode(arr[0])
  for (let i = 1; i < arr.length; i++) {
    const temp = new TreeNode(arr[i])
    head.next = temp
  }
  return head
};
