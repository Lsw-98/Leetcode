// 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
// 假设二叉树中至少有一个节点。

// 示例 1:
// 输入: root = [2, 1, 3]
// 输出: 1

// 示例 2:
// 输入: [1, 2, 3, 4, null, 5, 6, null, null, 7]
// 输出: 7


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
var findBottomLeftValue = function (root) {
  let maxNum = Infinity
  let maxLength = Infinity

  var backtrace = function (root, leftLen) {
    if (root.left === null && root.right === null) {
      if (leftLen > maxLength) {
        maxLength = leftLen
        maxNum = root.val
      }
    }

    if (root.left) {
      backtrace(root.left, leftLen + 1)
    }

    if (root.right) {
      backtrace(root.right, leftLen + 1)
    }

    return
  }

  backtrace(root, 0)
  return maxNum
};

