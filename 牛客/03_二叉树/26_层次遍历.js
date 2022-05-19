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
  * @return int整型二维数组
  */
function levelOrder(root) {
  const res = []
  if (root === null) {
    return res
  }

  const points = []
  points.push(root)
  while (points.length !== 0) {
    const result = []
    const size = points.length
    for (let i = 0; i < size; i++) {
      const temp = points.shift()
      result.push(temp.val)
      if (temp.left !== "#" && temp.left !== null) {
        points.push(temp.left)
      }
      if (temp.right !== "#" && temp.right !== null) {
        points.push(temp.right)
      }
    }
    res.push(result)
  }

  return res
}
module.exports = {
  levelOrder: levelOrder
};