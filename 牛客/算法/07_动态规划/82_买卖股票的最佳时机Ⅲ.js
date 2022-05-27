/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 * 两次交易所能获得的最大收益
 * @param prices int整型一维数组 股票每一天的价格
 * @return int整型
 */
function maxProfit(prices) {
  const res = new Array(prices.length).fill(0)
  for (let i = 1; i < prices.length; i++) {
    if (prices[i] > prices[i - 1]) {
      res[i] = prices[i] - prices[i - 1] + res[i - 1]
    }
  }
  res.sort()
  return res[res.length - 1] + res[res.length - 2]
}

module.exports = {
  maxProfit: maxProfit
};


console.log(maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]));
