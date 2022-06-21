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
function isCompleteTree(root) {
  const points = []
  points.push(root)
  let flag = false
  while (points.length !== 0) {
    const temp = points.shift()
    if (temp === null) flag = true
    else {
      if (flag) return false
      points.push(temp.left)
      points.push(temp.right)
    }
  }
  return true
}
module.exports = {
  isCompleteTree: isCompleteTree
};