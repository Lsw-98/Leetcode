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
 * @return {number[][]}
 */
var levelOrder = function (root) {
  const res = []
  if (root === null) {
    return res
  }

  function getVal(node) {
    if (node.left) {
      points.push(node.left)
    }
    if (node.right) {
      points.push(node.right)
    }
  }
  const points = []
  points.push(root)
  while (points.length !== 0) {
    const result = []
    const size = points.length
    for (let index = 0; index < size; index++) {
      const temp = points.shift()
      result.push(temp.val)
      getVal(temp)
    }

    res.push(result)
  }
  return res
};