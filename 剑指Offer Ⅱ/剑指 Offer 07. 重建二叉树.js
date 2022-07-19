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
      const targetValue = preorder[index]
      const targetIndex = arr.indexOf(targetValue)
      const newTree = new TreeNode(targetValue)

      if (targetIndex !== -1) {
        const leftArr = arr.slice(0, targetIndex)
        newTree.left = dfs(index + 1, leftArr)
        const rightArr = arr.slice(targetIndex + 1)
        newTree.right = dfs(index + 1 + leftArr.length, rightArr)
        return newTree
      }
    }
    return null
  }

  return dfs(0, inorder)
};