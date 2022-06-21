/*
 * function TreeNode(x) {
 *   this.val = x;
 *   this.left = null;
 *   this.right = null;
 * }
 */
/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 * 
 * @param root TreeNode类 
 * @return int整型一维数组
 */
function preorderTraversal(root) {
  const res = []
  if (root === null) return res
  function preOrder(node) {
    if (node.left !== "#" && node.left !== null) {
      preOrder(node.left)
    }
    res.push(node.val)
    if (node.right !== "#" && node.right !== null) {
      preOrder(node.right)
    }
  }

  preOrder(root)
  return res
}
module.exports = {
  preorderTraversal: preorderTraversal
};