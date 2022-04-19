// 给定一个二叉树，判断它是否是高度平衡的二叉树。
// 本题中，一棵高度平衡二叉树定义为：
// 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

// 示例 1：
// 输入：root = [3, 9, 20, null, null, 15, 7]
// 输出：true

// 示例 2
// 输入：root = [1, 2, 2, 3, 3, null, null, 4, 4]
// 输出：false

// 示例 3：
// 输入：root = []
// 输出：true


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
var isBalanced = function (root) {
  if (root === null) {
    return true
  }

  const points = []
  points.push(root)
  const res = []
  let flag = true
  let maxHeight = 0
  let minHeight = 0

  function getVal(node) {
    if (node.left) {
      points.push(node.left)
    }
    if (node.right) {
      points.push(node.right)
    }
  }

  while (points.length !== 0) {
    const size = points.length
    const result = []
    for (let index = 0; index < size; index++) {
      const temp = points.shift()
      if (temp.left === null && temp.right === null && flag) {
        minHeight = res.length + 1
        flag = false
      }
      result.push(temp.val)
      getVal(temp)
    }
    res.push(result)
  }

  maxHeight = res.length

  return !(maxHeight - minHeight > 1)
}