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
  if (root.left === null && root.right === null && root.val === sum) return true

  return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val)
}
module.exports = {
  hasPathSum: hasPathSum
};