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
  if (!root) {
    return false;
  }

  if (root.val == sum && root.left == null && root.right == null) {
    return true;
  }

  if (hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val)) {
    return true;
  } else {
    return false;
  }
}
module.exports = {
  hasPathSum: hasPathSum
};