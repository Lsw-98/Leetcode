function FindGreatestSumOfSubArray(array) {
  const dp = new Array(array.length).fill(0)
  dp[0] = array[0]

  for (let i = 1; i < array.length; i++) {
    dp[i] = Math.max(array[i], dp[i - 1] + array[i])
  }

  return Math.max(...dp)
}
module.exports = {
  FindGreatestSumOfSubArray: FindGreatestSumOfSubArray
};