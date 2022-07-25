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
 * @param {number} target
 * @return {number[][]}
 */
var pathSum = function (root, target) {
  const res = []
  const temp = [root.val]
  if (root === null) return res

  function backtrace(node, sum) {
    if (node.left === null && node.right === null && sum === target) {
      res.push(JSON.parse(JSON.stringify(temp)))
      return
    }

    if (node.left) {
      temp.push(node.left.val)
      sum += node.left.val
      backtrace(node.left, sum)
      sum -= node.left.val
      temp.pop()
    }
    if (node.right) {
      temp.push(node.right.val)
      sum += node.right.val
      backtrace(node.right, sum)
      sum -= node.right.val
      temp.pop()
    }
  }

  backtrace(root, root.val)
  return res
};