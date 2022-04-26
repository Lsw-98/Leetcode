// 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
// 差值是一个正数，其数值等于两值之差的绝对值。

// 示例 1：
// 输入：root = [4, 2, 6, 1, 3]
// 输出：1

// 示例 2：
// 输入：root = [1, 0, 48, null, null, 12, 49]
// 输出：1


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
var getMinimumDifference = function (root) {
  let pre = null
  let ans = 10000

  function inorder(node) {
    if (node === null) return
    inorder(node.left)
    if (pre !== null && Math.abs(pre.val - node.val) < ans) {
      ans = Math.abs(pre.val - node.val)
    }
    pre = node
    inorder(node.right)
    return ans
  }
  return inorder(root)
};