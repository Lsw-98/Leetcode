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
var inorderTraversal = function (root) {
  const res = []
  function getVal(root) {
    if (root !== null) {

      getVal(root.left)
      res.push(root.val)
      getVal(root.right)

    }
  }

  getVal(root)
  return res
};