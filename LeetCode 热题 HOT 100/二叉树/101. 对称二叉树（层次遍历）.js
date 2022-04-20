// 给你一个二叉树的根节点 root ， 检查它是否轴对称。 

// 示例 1：
// 输入：root = [1, 2, 2, 3, 4, 4, 3]
// 输出：true

// 示例 2：
// 输入：root = [1, 2, 2, null, 3, null, 3]
// 输出：false


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function (root) {
  if (root === null) return true

  let points = []
  points.push(root)
  while (points.length !== 0) {
    let res = []
    let size = points.length
    for (let index = 0; index < size; index++) {
      let temp = points.shift()
      if (temp === -999) {
        res.push(-999)
      } else {
        res.push(temp.val)
        if (temp.left) {
          points.push(temp.left)
        } else {
          points.push(-999)
        }
        if (temp.right) {
          points.push(temp.right)
        } else {
          points.push(-999)
        }
      }
    }
    if (res !== res.reverse()) return false
  }
  return true
};
