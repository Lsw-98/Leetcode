/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/**
 * @param {Node} root
 * @return {Node}
 */
var connect = function (root) {
  if (root === null) {
    return null
  }

  points = []
  points.push(root)

  function nextDir(node) {
    if (node.left) {
      points.push(node.left)
    }
    if (node.right) {
      points.push(node.right)
    }
  }

  while (points.length !== 0) {
    size = points.length
    for (let index = 0; index < size; index++) {
      point = points.shift()
      nextDir(point)
      if (index === size - 1) {
        break
      }

      point.next = points[0]
    }
  }
  return root
};