/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxValue = function (grid) {
  const dp = new Array(grid.length).fill(0).map(() => {
    return new Array(grid[0].length).fill(0)
  })

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (i === 0 && j === 0) {
        dp[i][j] = grid[i][j]
      } else if (i === 0 && j > 0) {
        dp[i][j] = dp[i][j - 1] + grid[i][j]
      } else if (j === 0 && i > 0) {
        dp[i][j] = dp[i - 1][j] + grid[i][j]
      } else {
        dp[i][j] = Math.max((grid[i][j] + dp[i - 1][j]), (grid[i][j] + dp[i][j - 1]))
      }
    }
  }

  return dp[dp.length - 1][dp[0].length - 1]
};

console.log(maxValue([[1, 3, 1], [1, 5, 1], [4, 2, 1]]));