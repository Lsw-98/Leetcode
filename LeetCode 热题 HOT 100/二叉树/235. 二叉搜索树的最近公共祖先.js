// 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

// 示例 1:
// 输入: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
// 输出: 6
// 解释: 节点 2 和节点 8 的最近公共祖先是 6。

// 示例 2:
// 输入: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
// 输出: 2
// 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。


/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  // 使用回溯，从下到上遍历
  function backtrace(root, p, q) {
    if (root === null || root === p || root === q) return root

    let left = backtrace(root.left, p, q)
    let right = backtrace(root.right, p, q)
    if (left !== null && right !== null) {
      return root
    }

    if (left === null) {
      return right
    }
    return left
  }

  return backtrace(root, p, q)
};