/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function (n) {
  let a = 0
  let b = 0
  let c = 0
  const dp = [1]
  for (let i = 1; i < n; i++) {
    dp[i] = Math.min(dp[a] * 2, dp[b] * 3, dp[c] * 5)
    if (dp[i] === dp[a] * 2) a += 1

    if (dp[i] === dp[b] * 3) b += 1

    if (dp[i] === dp[c] * 5) c += 1
  }
  return dp[dp.length - 1]
}
