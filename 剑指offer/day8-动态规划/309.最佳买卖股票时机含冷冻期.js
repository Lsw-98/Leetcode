/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let res = 0
  if (prices.length < 2) {
    return res
  }

  const dp = new Array(prices.length).fill(0)
  dp[0] = 0
  let flag = false
  let minNum = 0

  for (let i = 1; i < prices.length; i++) {
    if (flag) {
      flag = false
      if (i < prices.length - 1) {
        minNum = i + 1
      }
      continue
    }
    if (prices[i] > prices[i - 1]) {
      dp[i] = Math.max(prices[i] - prices[i - 1], prices[i] - prices[minNum])
      flag = true
    }
  }

  return res
};

console.log(maxProfit([1, 2, 4]))