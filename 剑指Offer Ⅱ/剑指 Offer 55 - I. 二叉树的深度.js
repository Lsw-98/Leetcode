/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function (root) {
  let max = 0
  let temp = 1
  if (root === null) return max

  function bakctrace(node) {
    if (node.left === null && node.right === null && max < temp) {
      max = temp
      return
    }

    if (node.left) {
      temp += 1
      bakctrace(node.left)
      temp -= 1
    }
    if (node.right) {
      temp += 1
      bakctrace(node.right)
      temp -= 1
    }
  }

  bakctrace(root)
  return max
};