/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
  const res = []
  if (root === null) return res
  let flag = 0
  const points = []
  points.push(root)
  while (points.length) {
    const size = points.length
    const result = []
    for (let i = 0; i < size; i++) {
      const temp = points.shift()
      if (flag) result.unshift(temp.val)
      else result.push(temp.val)
      if (temp.left) points.push(temp.left)
      if (temp.right) points.push(temp.right)
    }
    flag = !flag
    res.push(result)
  }
  return res
};