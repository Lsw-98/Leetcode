/* function TreeNode(x) {
    this.val = x;
    this.left = null;
    this.right = null;
} */
function Print(pRoot) {
  const res = []
  if (pRoot === null) {
    return res
  }

  const points = []
  points.push(pRoot)
  let count = 1

  while (points.length > 0) {
    const result = []
    const size = points.length
    for (let i = 0; i < size; i++) {
      const temp = points.shift()
      result.push(temp.val)
      if (temp.left !== "#" && temp.left !== null) {
        points.push(temp.left)
      }
      if (temp.right !== "#" && temp.right !== null) {
        points.push(temp.right)
      }
    }
    if (count === 1) {
      res.push(result)
      count = 2
    } else {
      count = 1
      const temp = result.reverse()
      res.push(temp)
    }

  }

  return res
}
module.exports = {
  Print: Print
};