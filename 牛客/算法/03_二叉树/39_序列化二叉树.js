/* function TreeNode(x) {
    this.val = x;
    this.left = null;
    this.right = null;
} */
function Serialize(pRoot) {
  if (pRoot === null) return ""
  const points = []
  points.push(pRoot)
  let s = ""
  s += pRoot.val + "!"
  while (points.length !== 0) {
    const size = points.length
    for (let i = 0; i < size; i++) {
      const temp = points.shift()
      if (temp.left) {
        s += temp.left.val + "!"
        points.push(temp.left)
      } else {
        s += "#!"
      }
      if (temp.right) {
        s += temp.right.val + "!"
        points.push(temp.right)
      } else {
        s += "#!"
      }
    }
  }
  return s
}
function Deserialize(s) {
  if (s === "") return null
  s = s.split("!")
  // 将最后一个空字符串pop()出
  s.pop()
  let i = 1
  let root = new TreeNode(Number(s[0]))
  let queue = [root]
  while (i < s.length) {
    let font = queue.shift()
    if (s[i] !== '#') {
      font.left = new TreeNode(Number(s[i]))
      queue.push(font.left)
    }
    i++

    if (s[i] !== '#') {
      font.right = new TreeNode(Number(s[i]))
      queue.push(font.right)
    }
    i++
  }
  return root
}
module.exports = {
  Serialize: Serialize,
  Deserialize: Deserialize
};