/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDepth = function (root) {
  function getDepth(node) {
    if (node === null) return 0
    let leftDepth = getDepth(node.left)
    let rightDepth = getDepth(node.right)

    if (node.left === null && node.right !== null) {
      return 1 + rightDepth
    }

    if (node.left !== null && node.right === null) {
      return 1 + leftDepth
    }

    let res = 1 + Math.min.call(null, leftDepth, rightDepth)
    return res
  }

  return getDepth(root)
};