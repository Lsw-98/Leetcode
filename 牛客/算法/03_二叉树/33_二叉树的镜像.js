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
 * @param pRoot TreeNode类 
 * @return TreeNode类
 */
function Mirror(pRoot) {
  if (pRoot === null) return null

  pRoot.mid = pRoot.left
  pRoot.left = pRoot.right
  pRoot.right = pRoot.mid
  Mirror(pRoot.left)
  Mirror(pRoot.right)

  return pRoot
}
module.exports = {
  Mirror: Mirror
};