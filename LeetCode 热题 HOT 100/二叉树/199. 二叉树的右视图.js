/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var rightSideView = function (root) {
  ans = []
  if (root === null) {
    return ans
  }
  res = []
  function getVal(node) {
    if (node.left) {
      points.push(node.left)
    }

    if (node.right) {
      points.push(node.right)
    }
  }

  points = []
  points.push(root)
  while (points.length !== 0) {
    size = points.length
    result = []
    for (let index = 0; index < size; index++) {
      temp = points.shift()
      result.push(temp.val)
      getVal(temp)
    }
    res.push(result)
  }

  for (let i in res){
    ans.push(res[i][res[i].length - 1])
  }
  return ans
};