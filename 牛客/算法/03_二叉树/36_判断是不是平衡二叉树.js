/* function TreeNode(x) {
    this.val = x;
    this.left = null;
    this.right = null;
} */
function IsBalanced_Solution(pRoot) {
  function height(node) {
    if (node === null) return 0
    const leftHeight = height(node.left)
    const rightHeight = height(node.right)

    if (leftHeight === -1 || rightHeight === -1 || Math.abs(leftHeight - rightHeight) + 1) {
      return -1
    } else {
      return Math.max(leftHeight, rightHeight) + 1
    }
  }

  return height(pRoot) >= 1
}
module.exports = {
  IsBalanced_Solution: IsBalanced_Solution
};