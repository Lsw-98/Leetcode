/**
 * 
 * @param matrix int整型二维数组 the matrix
 * @return int整型
 */
function minPathSum(matrix) {
  const dp = new Array(matrix.length).fill(0).map(item => {
    return new Array(matrix[0].length).fill(0)
  })

  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      if (i === 0 && j === 0) {
        dp[i][j] = matrix[i][j]
      } else if (i === 0) {
        dp[i][j] = dp[i][j - 1] + matrix[i][j]
      } else if (j === 0) {
        dp[i][j] = dp[i - 1][j] + matrix[i][j]
      }
    }
  }

  for (let i = 1; i < matrix.length; i++) {
    for (let j = 1; j < matrix[i].length; j++) {
      dp[i][j] = Math.min(dp[i - 1][j] + matrix[i][j], dp[i][j - 1] + matrix[i][j])
    }
  }
  return dp[dp.length - 1][dp[0].length - 1]
}
module.exports = {
  minPathSum: minPathSum
};

console.log(minPathSum([[1, 3, 5, 9], [8, 1, 3, 4], [5, 0, 6, 1], [8, 8, 4, 0]]));
console.log(minPathSum([[1, 2, 3], [1, 2, 3]]));