/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
  res = []
  if (root === null) {
    return res
  }

  function getVal(node) {
    if (node.children) {
      for (let item of node.children) {
        points.push(item)
      }
    }
  }

  points = []
  points.push(root)

  while (points.length !== 0) {
    result = []
    size = points.length
    for (let index = 0; index < size; index++) {
      temp = points.shift()
      result.push(temp.val)
      getVal(temp)
    }

    res.push(result)
  }
  return res

};
