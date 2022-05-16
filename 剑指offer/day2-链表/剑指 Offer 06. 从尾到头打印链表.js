// 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。 

// 示例 1：
// 输入：head = [1, 3, 2]
// 输出：[2, 3, 1]


/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {number[]}
 */
// 使用splice方法
// var reversePrint = function (head) {
//   const res = []

//   while (head) {
//     res.splice(0, 0, head.val)
//     head = head.next
//   }
//   return res
// };

// 先反转链表，再遍历
var reversePrint = function (head) {
  const res = []
  let cur = head
  let pre = null
  while (cur) {
    let temp = cur.next
    cur.next = pre
    pre = cur
    cur = temp
  }

  while (pre) {
    res.push(pre.val)
    pre = pre.next
  }
  return res
};

// 使用栈
