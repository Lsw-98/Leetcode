function jumpFloor(number) {
  const dp = []
  dp.push(1)
  dp.push(1)

  for (let i = 2; i <= number; i++) {
    dp[i] = dp[i - 1] + dp[i - 2]
  }
  return dp[dp.length - 1]
}
module.exports = {
  jumpFloor: jumpFloor
};