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
var maxDepth = function (root) {
  let result = 0
  if (root === null) return result
  function preOrder(node, depth) {
    result = depth > result ? depth : result
    if (node.left === null && node.right === null) {
      return
    }
    if (node.left) {
      preOrder(node.left, depth + 1)
    }
    if (node.right) {
      preOrder(node.right, depth + 1)
    }
  }

  preOrder(root, 1)
  return result
};