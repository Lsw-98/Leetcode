function levelorder(root) {
  const res = []

  if (root === null) return res

  const points = []
  points.push(root)
  while (points.length !== 0) {
    const size = points.length
    const result = []
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
    res.push(result)
  }
  return res
}