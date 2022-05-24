/**
  * 
  * @param m int整型 
  * @param n int整型 
  * @return int整型
  */
function uniquePaths(m, n) {
  let dp = new Array(m).fill(1).map(item => {
    return new Array(n).fill(1)
  })

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    }
  }

  return dp[m - 1][n - 1]
}
module.exports = {
  uniquePaths: uniquePaths
};


console.log(uniquePaths(2, 1));
console.log(uniquePaths(2, 2));
