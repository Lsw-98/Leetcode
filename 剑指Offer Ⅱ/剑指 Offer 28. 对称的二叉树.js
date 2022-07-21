/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function (root) {
  if (root === null) {
    return true
  }

  const points = []
  points.push(root)
  let flag = false
  let num = 0
  while (points.length !== 0) {
    const result = []
    const size = points.length
    for (let i = 0; i < size; i++) {
      if (num > 0) {
        flag = true
      }
      const temp = points.shift()
      if (temp === 1001) {
        result.push(1001)
        continue
      }
      result.push(temp.val)
      if (temp.left !== null) {
        points.push(temp.left)
      } else {
        points.push(1001)
      }
      if (temp.right !== null) {
        points.push(temp.right)
      } else {
        points.push(1001)
      }
    }
    let left = 0
    let right = result.length - 1
    while (left <= right) {
      if (result[left] !== result[right]) {
        return false
      }
      left += 1
      right -= 1
    }
  }
  return true
}
