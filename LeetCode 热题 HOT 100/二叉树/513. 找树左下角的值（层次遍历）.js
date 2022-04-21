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
  let res = 0
  if (root === null) {
    return res
  }

  const points = []
  points.push(root)
  while (points.length !== 0) {
    const size = points.length
    for (let index = 0; index < size; index++) {
      const temp = points.shift()
      if (index === 0) {
        res = temp.val
      }
      if (temp.left) {
        points.push(temp.left)
      }
      if (temp.right) {
        points.push(temp.right)
      }
    }

  }
  return res
};

