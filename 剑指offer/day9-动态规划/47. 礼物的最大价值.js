// 在一个 m * n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
// 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
// 给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

// 示例 1:
// 输入:
// [
//   [1, 3, 1],
//   [1, 5, 1],
//   [4, 2, 1]
// ]
// 输出: 12
// 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物


/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxValue = function (grid) {
  const dp = []
  for (let i = 0; i < grid.length; i++) {
    const temp = []
    for (let j = 0; j < grid[i].length; j++) {
      temp.push(0)
    }
    dp.push(temp)
  }

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (i === 0 && j === 0) {
        dp[i][j] = grid[i][j]
      } else if (i === 0) {
        dp[i][j] = dp[i][j - 1] + grid[i][j]
      } else if (j === 0) {
        dp[i][j] = dp[i - 1][j] + grid[i][j]
      } else {
        dp[i][j] = Math.max.call(null, grid[i][j] + dp[i - 1][j], grid[i][j] + dp[i][j - 1])
      }
    }
  }
  return dp[dp.length - 1][dp[dp.length - 1].length - 1]
};


console.log(maxValue([
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]));