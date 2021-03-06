// 给定二叉树的根节点 root ，返回所有左叶子之和。

// 示例 1：
// 输入: root = [3, 9, 20, null, null, 15, 7]
// 输出: 24
// 解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

// 示例 2:
// 输入: root = [1]
// 输出: 0


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
 * @return {number}
 */
var sumOfLeftLeaves = function (root) {
  let res = 0
  if (root === null) return res
  if (root.left === null && root.right === null) return 0

  const points = []
  points.push(root)
  while (points.length !== 0) {
    const size = points.length
    for (let index = 0; index < size; index++) {
      const temp = points.shift()
      if (temp === 0) {

      } else {
        if (temp.left === null && temp.right === null) {
          if (index % 2 === 0) {
            res += temp.val
          }
        } else {
          if (temp.left) {
            points.push(temp.left)
          } else {
            points.push(0)
          }
          if (temp.right) {
            points.push(temp.right)
          } else {
            points.push(0)
          }
        }
      }
    }
  }
  return res
};