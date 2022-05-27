function Fibonacci(n) {
  const dp = []
  dp.push(1)
  dp.push(1)

  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2]
  }
  return dp[dp.length - 1]
}
module.exports = {
  Fibonacci: Fibonacci
};

console.log(Fibonacci(7));