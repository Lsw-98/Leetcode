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
 * @param {number} targetSum
 * @return {number[][]}
 */
var pathSum = function (root, targetSum) {
  const res = []
  const temp = []
  if (root === null) return res

  temp.push(root.val)
  if (root.left === null && root.right === null && targetSum === root.val) {
    return [temp]
  }

  function backtrace(node, count) {
    if (node.left === null && node.right === null && count === targetSum) {
      res.push(JSON.parse(JSON.stringify(temp)))
      return
    }

    if (node.left) {
      count += node.left.val
      temp.push(node.left.val)
      backtrace(node.left, count)
      temp.pop()
      count -= node.left.val
    }

    if (node.right) {
      count += node.right.val
      temp.push(node.right.val)
      backtrace(node.right, count)
      temp.pop()
      count -= node.right.val
    }
  }

  backtrace(root, root.val)
  return res
};