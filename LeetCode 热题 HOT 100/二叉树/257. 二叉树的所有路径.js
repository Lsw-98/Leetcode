// 给你一个二叉树的根节点 root ，按任意顺序 ，返回所有从根节点到叶子节点的路径。
// 叶子节点 是指没有子节点的节点。

// 示例 1：
// 输入：root = [1, 2, 3, null, 5]
// 输出：["1->2->5", "1->3"]

// 示例 2：
// 输入：root = [1]
// 输出：["1"]


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
 * @return {string[]}
 */
var binaryTreePaths = function (root) {
  const res = []
  if (root === null) {
    return res
  }

  function backtrace(node, str) {
    if (node.left === null && node.right === null) {
      str += node.val
      res.push(str)
      return
    }

    str += node.val + "->"

    if (node.left) {
      backtrace(node.left, str)
    }

    if (node.right) {
      backtrace(node.right, str)
    }
  }

  backtrace(root, '')
  return res
};