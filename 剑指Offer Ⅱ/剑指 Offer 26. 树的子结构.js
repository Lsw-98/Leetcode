/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} A
 * @param {TreeNode} B
 * @return {boolean}
 */
var isSubStructure = function (A, B) {
  // 2. 递归判断传入函数的节点进行比较
  function travesal(rootA, rootB) {
    // 2.1 判断 B 子树是否为空，*A*处在传入时候先判断 B 是否为空，这里相当于判断的是 B 的子树
    if (!rootB) return true;
    // 2.2 当前节点为空，则不相等
    if (!rootA) return false;
    // 2.3 值不相等则结构不同
    if (rootA.val !== rootB.val) return false;
    // 2.4 递归判断下一个子树
    return travesal(rootA.left, rootB.left) && travesal(rootA.right, rootB.right);
  }
  // 1. 约定空树不是任意一个树的子结构
  if (!A || !B) return false;// *A*
  // 3. 先递归跟节点，在依次比较左节点和右边节点（只要A树的任意一个节点开始和B树相同，则B树为A树的子结构）
  return travesal(A, B) || isSubStructure(A.left, B) || isSubStructure(A.right, B);

};
