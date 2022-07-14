/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} A
 * @param {TreeNode} B
 * @return {boolean}
 */
var isSubStructure = function (A, B) {
  if (A === null || B === null) return false
  function preOrder(node) {
    if (node.val === B.val) {
      return node
    }
    if (node) {
      preOrder(node.left)
      preOrder(node.right)
    }
  }

  preOrder(A)
};