/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 * 计算最大收益
 * @param prices int整型一维数组 股票每一天的价格
 * @return int整型
 */
function maxProfit(prices) {
  let res = 0
  let minPrice = prices[0]
  for (let i = 1; i < prices.length; i++) {
    if (prices[i] > minPrice) {
      res += prices[i] - minPrice
    }
    minPrice = prices[i]
  }
  return res
}
module.exports = {
  maxProfit: maxProfit
};

console.log(maxProfit([8, 9, 2, 5, 4, 7, 1]));
console.log(maxProfit([5, 4, 3, 2, 1]));
console.log(maxProfit([1, 2, 3, 4, 5]));