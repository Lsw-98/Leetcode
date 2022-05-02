// 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

// 每行的元素从左到右升序排列。
// 每列的元素从上到下升序排列。

// 示例 1：
// 输入：matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], target = 5
// 输出：true

// 示例 2：
// 输入：matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], target = 20
// 输出：false


/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
  // for (let i = 0; i < matrix.length; i++) {
  //   for (let j = 0; j < matrix[i].length; j++) {
  //     if (matrix[i][j] > target) {
  //       break
  //     } else if (matrix[i][j] === target) {
  //       return true
  //     }
  //   }
  // }
  // return false

  // for (let i = 0; i < matrix.length; i++) {
  //   let left = 0
  //   let right = matrix[i].length - 1
  //   while (left <= right) {
  //     if (matrix[i][left] === target || matrix[i][right] === target) {
  //       return true
  //     } else if (matrix[i][left] > target || matrix[i][right] > target) {
  //       break
  //     }
  //     left += 1
  //     right -= 1
  //   }
  // }
  // return false

  let right = matrix[0].length - 1, left = 0;
  while (right >= 0 && left < matrix.length) {
    if (matrix[left][right] > target) {
      right--;
    } else if (matrix[left][right] < target) {
      left++;
    } else {
      return true;
    }
  }
  return false;
}


console.log(searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5));
console.log(searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20));
