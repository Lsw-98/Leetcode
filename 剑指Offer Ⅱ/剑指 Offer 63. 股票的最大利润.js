/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let min = prices[0]
  const dp = new Array(prices.length).fill(0)
  for (let i = 1; i < dp.length; i++) {
    if (prices[i] < min) {
      min = prices[i]
    } else {
      dp[i] = prices[i] - min
    }
  }
  return Math.max(...dp)
};

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
console.log(maxProfit([7, 6, 4, 3, 1]));