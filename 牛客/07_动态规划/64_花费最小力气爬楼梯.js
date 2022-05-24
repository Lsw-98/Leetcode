/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param cost int整型一维数组 
 * @return int整型
 */
function minCostClimbingStairs(cost) {
  const dp = []
  dp.push(cost[0])
  dp.push(cost[1])

  for (let i = 2; i < cost.length; i++) {
    dp[i] = Math.min.call(null, dp[i - 1] + cost[i], dp[i - 2] + cost[i])
  }
  return Math.min.call(null, dp[dp.length - 1], dp[dp.length - 2])
}
module.exports = {
  minCostClimbingStairs: minCostClimbingStairs
};


console.log(minCostClimbingStairs([2, 5, 20]));
console.log(minCostClimbingStairs([1, 100, 1, 1, 1, 90, 1, 1, 80, 1]));
