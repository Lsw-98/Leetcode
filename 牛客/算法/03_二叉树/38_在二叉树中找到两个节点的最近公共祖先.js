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
 * @param o1 int整型 
 * @param o2 int整型 
 * @return int整型
 */
function lowestCommonAncestor(root, o1, o2) {
  if (root === null) { return null }
  if (root.val === o1 || root.val === o2) { return root.val } //查找到o1或o2节点 返回值
  let left = lowestCommonAncestor(root.left, o1, o2) //left记录左边子树寻找的结果
  let right = lowestCommonAncestor(root.right, o1, o2) //right记录右边子树寻找的结果
  //如果o1、o2在两侧，对于栈顶的当前函数root的left和right都有值
  if (left && right) { return root.val }
  //如果单侧有值，返回这个值，如果到最后没有经历上面一行的代码，说明这个值就是最近公共祖先
  if (left) { return left }
  if (right) { return right }
}
module.exports = {
  lowestCommonAncestor: lowestCommonAncestor
};