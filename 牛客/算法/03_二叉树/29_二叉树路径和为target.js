/*
 * function TreeNode(x) {
 *   this.val = x;
 *   this.left = null;
 *   this.right = null;
 * }
 */

/**
  * 
  * @param root TreeNode类 
  * @param sum int整型 
  * @return bool布尔型
  */
function hasPathSum(root, sum) {
  if (root === null) return false

  function getPath(node, count) {
    if (node.left === null && node.right === null && count === sum) {
      return true
    }

    if (node.left === null && node.right === null) {
      return false
    }

    if (node.left !== "#" && node.left !== null) {
      return getPath(root.left, node.left.val)
    }
    if (node.right !== "#" && node.right !== null) {
      return getPath(node.right, node.right.val)
    }

    return false
  }
  return getPath(root, root.val)
}
module.exports = {
  hasPathSum: hasPathSum
};