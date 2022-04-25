// 给你两棵二叉树： root1 和 root2 。
// 想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。
// 你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；
// 否则，不为 null 的节点将直接作为新二叉树的节点。
// 返回合并后的二叉树。
// 注意: 合并过程必须从两个树的根节点开始。

// 示例 1：
// 输入：root1 = [1, 3, 2, 5], root2 = [2, 1, 3, null, 4, null, 7]
// 输出：[3, 4, 5, 5, 4, null, 7]

// 示例 2：
// 输入：root1 = [1], root2 = [1, 2]
// 输出：[2, 2]


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {TreeNode}
 */
var mergeTrees = function (root1, root2) {
  if (root1 === null) return root2
  if (root2 === null) return root1

  let queue = []
  queue.push(root1)
  queue.push(root2)

  while (queue.length !== 0) {
    const temp1 = queue.shift()
    const temp2 = queue.shift()
    temp1.val += temp2.val

    if (temp1.left !== null && temp2.left !== null) {
      queue.push(temp1.left)
      queue.push(temp2.left)
    }
    if (temp1.right !== null && temp2.right !== null) {
      queue.push(temp1.right)
      queue.push(temp2.right)
    }
    if (temp1.left === null && temp2.left !== null) {
      temp1.left = temp2.left
    }
    if (temp1.right === null && temp2.right !== null) {
      temp1.right = temp2.right
    }
  }

  return root1
};