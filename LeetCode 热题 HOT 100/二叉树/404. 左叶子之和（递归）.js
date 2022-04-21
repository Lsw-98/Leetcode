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
  if (root === null) {
    return 0
  }

  let leftValue = sumOfLeftLeaves(root.left)
  let rightValue = sumOfLeftLeaves(root.right)
  let midValue = 0

  if (root.left && root.left.left === null && root.left.right === null) {
    midValue += root.left.val
  }

  let sum = midValue + leftValue + rightValue

  return sum
};