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
 * @return {number[]}
 */
var largestValues = function (root) {
  res = []
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
  points = []
  points.push(root)
  while (points.length !== 0) {
    result = []
    size = points.length
    for (let index = 0; index < size; index++) {
      temp = points.shift()
      result.push(temp.val)
      getVal(temp)
    }

    res.push(Math.max.apply(null, result))
  }
  return res
};