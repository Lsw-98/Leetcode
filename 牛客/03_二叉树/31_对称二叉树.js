/* function TreeNode(x) {
    this.val = x;
    this.left = null;
    this.right = null;
} */
function isSymmetrical(pRoot) {
  if (pRoot === null) {
    return true
  }

  const points = []
  points.push(pRoot)
  let flag = false
  while (points.length !== 0) {
    const result = []
    const size = points.length
    for (let i = 0; i < size; i++) {
      if (i > 0) {
        flag = true
      }
      const temp = points.shift()
      if (temp === 1001) {
        continue
      }
      result.push(temp.val)
      if (temp.left !== "#" && temp.left !== null) {
        points.push(temp.left)
      } else {
        points.push(1001)
      }
      if (temp.right !== "#" && temp.right !== null) {
        points.push(temp.right)
      } else {
        points.push(1001)
      }
    }
    if (result.length === 1 && flag) {
      return false
    } else {
      const res = result.reverse()
      res === result
    }
  }
  return true
}
module.exports = {
  isSymmetrical: isSymmetrical
};