// 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

// 有效 二叉搜索树定义如下：
// 节点的左子树只包含 小于 当前节点的数。
// 节点的右子树只包含 大于 当前节点的数。
// 所有左子树和右子树自身必须也是二叉搜索树。

// 示例 1：
// 输入：root = [2, 1, 3]
// 输出：true

// 示例 2：
// 输入：root = [5, 1, 4, null, null, 3, 6]
// 输出：false
// 解释：根节点的值是 5 ，但是右子节点的值是 4 。


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
 * @return {boolean}
 */
var isValidBST = function (root) {
  // 中序遍历是一个有序的数组，那么就是合法的
  const res = []

  function midOrder(node) {
    if (node !== null) {
      midOrder(node.left)
      res.push(node.val)
      midOrder(node.right)
    }
  }

  midOrder(root)
  const ans = JSON.parse(JSON.stringify(res))
  res.sort()

  return ans === res
};
