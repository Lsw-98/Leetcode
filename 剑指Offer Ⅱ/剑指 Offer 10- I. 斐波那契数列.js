/**
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
  const dp = [0, 1]
  if (n === 0) return dp[0]
  if (n === 1) return dp[1]

  for (let i = 2; i <= n; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
  }
  return dp[dp.length - 1]
};


console.log(fib(45));
