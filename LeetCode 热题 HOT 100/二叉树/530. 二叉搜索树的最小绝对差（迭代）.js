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
  let ans = 100000
  const res = []

  function inorder(node) {
    if (node === null) {
      return
    }

    inorder(node.left)
    res.push(node.val)
    inorder(node.right)
  }

  inorder(root)
  for (let index = 1; index < res.length; index++) {
    if (res[index] - res[index - 1] < ans) {
      ans = res[index] - res[index - 1]
    }

  }
  return ans
};