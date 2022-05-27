/**
  * 
  * @param prices int整型一维数组 
  * @return int整型
  */
function maxProfit(prices) {
  let dp = new Array(prices.length).fill(0)
  let minPrice = prices[0]
  for (let i = 1; i < prices.length; i++) {
    if (prices[i] > minPrice) {
      dp[i] = prices[i] - minPrice
    } else {
      minPrice = prices[i]
    }
  }
  return Math.max(...dp)
}
module.exports = {
  maxProfit: maxProfit
};

console.log(maxProfit([8, 9, 2, 5, 4, 7, 1]));