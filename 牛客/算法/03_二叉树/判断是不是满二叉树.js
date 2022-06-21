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
  // 层次遍历+统计节点个数
  const points = []
  points.push(root)
  let count = 0
  const res = []
  while (points.length !== 0) {
    const size = points.length
    const result = []
    for (let i = 0; i < size; i++) {
      const temp = points.shift()
      if (temp.left !== "#" && temp.left !== null) {
        points.push(temp.left)
      }
      if (temp.right !== "#" && temp.right !== null) {
        points.push(temp.right)
      }
    }
    count += result.length
    res.push(result)
  }
  if (count === Math.pow(2, res.length) - 1) {
    return true
  }
  return false
}
module.exports = {
  isCompleteTree: isCompleteTree
};