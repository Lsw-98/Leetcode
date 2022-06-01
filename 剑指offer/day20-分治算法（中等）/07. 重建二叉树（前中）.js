/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {

  function dfs(index, arr) {
    if (index < preorder.length) {
      const targetVal = preorder[index]
      const targetIndex = arr.indexOf(targetVal)
      const newRoot = new TreeNode(targetVal)

      if (targetIndex !== -1) {
        const leftArr = arr.slice(0, targetIndex)
        newRoot.left = dfs(index + 1, leftArr)
        const rightArr = arr.slice(targetIndex + 1)
        newRoot.right = dfs(index + leftArr.length + 1, rightArr)
        return newRoot
      }
    }
    return null
  }

  return dfs(0, inorder)
};