/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthLargest = function (root, k) {
  let res = []
  if (root === null) return 0
  function midorder(node) {
    if (node.left) midorder(node.left)
    res.push(node.val)
    if (node.right) midorder(node.right)
  }
  midorder(root)
  return res[res.length - k]
};