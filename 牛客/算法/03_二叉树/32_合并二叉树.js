/*
 * function TreeNode(x) {
 *   this.val = x;
 *   this.left = null;
 *   this.right = null;
 * }
 */

/**
 * 
 * @param t1 TreeNodeš▒╗ 
 * @param t2 TreeNodeš▒╗ 
 * @return TreeNodeš▒╗
 */
function mergeTrees(t1, t2) {
  if (t1 && t2) {
    t1.val += t2.val
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)
  }

  return t1 || t2
}
module.exports = {
  mergeTrees: mergeTrees
};