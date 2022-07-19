/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var findNumberIn2DArray = function (matrix, target) {
  let row = 0
  let column = matrix[0].length - 1
  while (row < matrix.length && column >= 0) {
    if (matrix[row][column] === target) {
      return true
    } else if (matrix[row][column] > target) {
      column -= 1
    } else {
      row += 1
    }
  }
  return false
};

console.log(findNumberIn2DArray([
  [-1, 3]
], 3))

console.log(findNumberIn2DArray([
  [1, 4, 7, 11, 15],
  [2, 5, 8, 12, 19],
  [3, 6, 9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 5))
console.log(findNumberIn2DArray([
  [1, 4, 7, 11, 15],
  [2, 5, 8, 12, 19],
  [3, 6, 9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 20))