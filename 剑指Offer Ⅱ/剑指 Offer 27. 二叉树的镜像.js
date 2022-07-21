/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var mirrorTree = function (root) {
  const res = root
  if (root === null) { return res }
  function preorder(node) {
    const temp = node.left
    node.left = node.right
    node.right = temp
    if (node.left) preorder(node.left)
    if (node.right) preorder(node.right)
  }
  preorder(root)
  return res
};