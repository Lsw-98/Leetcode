/* function TreeNode(x) {
    this.val = x;
    this.left = null;
    this.right = null;
} */
function reConstructBinaryTree(pre, vin) {
  function dfs(index, arr) {
    if (index < pre.length) {
      const targetVal = pre[index]
      const targetIndex = arr.indexOf(targetVal)
      const newRoot = new TreeNode(targetVal)

      if (targetIndex !== -1) {
        const leftArr = arr.slice(0, targetIndex)
        newRoot.left = dfs(index + 1, leftArr)
        const rightArr = arr.slice(targetIndex + 1)
        newRoot.right = dfs(index + 1 + leftArr.length, rightArr)
        return newRoot
      }
    }
    return null
  }

  return dfs(0, vin)
}
module.exports = {
  reConstructBinaryTree: reConstructBinaryTree
};