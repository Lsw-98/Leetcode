/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 * 求二叉树的右视图
 * @param xianxu int整型一维数组 先序遍历
 * @param zhongxu int整型一维数组 中序遍历
 * @return int整型一维数组
 */
function solve(xianxu, zhongxu) {
  const res = []
  let newTree = new TreeNode()

  function dfs(index, arr) {
    if (index < xianxu.length) {
      const targetVal = xianxu[index]
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

  newTree = dfs(0, zhongxu)
  if (newTree === null) return res
  const points = []
  points.push(newTree)
  while (points.length !== 0) {
    const result = []
    const size = points.length
    for (let i = 0; i < size; i++) {
      const temp = points.shift()
      result.push(temp.val)
      if (temp.left) {
        points.push(temp.left)
      }
      if (temp.right) {
        points.push(temp.right)
      }
    }
    res.push(result[result.length - 1])
  }

  return res
}
module.exports = {
  solve: solve
};