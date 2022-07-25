/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var levelOrder = function (root) {
  const res = []
  if (root === null) return res

  const points = []
  points.push(root)
  while (points.length) {
    const size = points.length
    for (let i = 0; i < size; i++) {
      const temp = points.shift()
      res.push(temp.val)
      if (temp.left) points.push(temp.left)
      if (temp.right) points.push(temp.right)
    }
  }
  return res
};