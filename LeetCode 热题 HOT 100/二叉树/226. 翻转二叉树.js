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
 * @return {TreeNode}
 */
var invertTree = function (root) {
  if (root === null) {
    return null
  }

  points = []
  points.push(root)
  while (points.length !== 0) {
    size = points.length
    for (let index = 0; index < size; index++) {
      temp = points.shift()
      if (temp.left) {
        points.push(temp.left)
      }
      if (temp.right) {
        points.push(temp.right)
      }
      tempChange = temp.left
      temp.left = temp.right
      temp.right = tempChange
    }
  }
  return root
};