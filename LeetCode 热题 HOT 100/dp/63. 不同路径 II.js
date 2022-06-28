/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function (obstacleGrid) {
  const m = obstacleGrid.length
  const n = obstacleGrid[0].length
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (obstacleGrid[i][j] === 1) {
        obstacleGrid[i][j] = "#"
      }
    }
  }

  if (obstacleGrid[m - 1][n - 1] === "#" || obstacleGrid[0][0] === "#") {
    return 0
  }

  let iflag = false
  let jflag = false

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (i === 0) {
        if (iflag) {
          obstacleGrid[i][j] = 0
          continue
        }
        if (obstacleGrid[i][j] !== "#") {
          obstacleGrid[i][j] = 1
        } else {
          iflag = true
        }
        continue
      }
      if (j === 0) {
        if (jflag) {
          obstacleGrid[i][j] = 0
          continue
        }
        if (obstacleGrid[i][j] !== "#") {
          obstacleGrid[i][j] = 1
        } else {
          jflag = true
        }
        continue
      }
      if (obstacleGrid[i][j] !== "#") {
        if (obstacleGrid[i - 1][j] === "#" && obstacleGrid[i][j - 1] === "#") {
          obstacleGrid[i][j] = 0
        } else if (obstacleGrid[i - 1][j] === "#") {
          obstacleGrid[i][j] = obstacleGrid[i][j - 1]
        } else if (obstacleGrid[i][j - 1] === "#") {
          obstacleGrid[i][j] = obstacleGrid[i - 1][j]
        } else {
          obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        }
      }
    }
  }
  return obstacleGrid[m - 1][n - 1]
};


console.log(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
