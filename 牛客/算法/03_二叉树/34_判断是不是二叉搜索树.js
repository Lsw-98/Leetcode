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
 * 
 * @param root TreeNode类 
 * @return bool布尔型
 */
function isValidBST(root) {
  // 中序遍历一定是递增的
  const res = []

  function midOrder(node) {
    if (node.left !== "#" && node.left) midOrder(node.left)
    res.push(node.val)
    if (node.right !== "#" && node.right) midOrder(node.right)
  }

  midOrder(root)
  for (let i = 1; i < res.length; i++) {
    if (res[i] < res[i - 1]) return false
  }
  return true
}
module.exports = {
  isValidBST: isValidBST
};