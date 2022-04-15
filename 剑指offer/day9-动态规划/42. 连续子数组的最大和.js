// 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
// 要求时间复杂度为O(n)。

// 示例1:
// 输入: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
// 输出: 6
// 解释: 连续子数组[4, -1, 2, 1] 的和最大，为 6。


/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  if (nums.length === 0) {
    return 0
  }
  if (nums.length === 1) {
    return nums[0]
  }
  const dp = []
  for (let index = 0; index < nums.length; index++) {
    dp.push(0)
  }
  dp[0] = nums[0]
  for (const i in nums) {
    if (dp[i - 1] > 0) {
      dp[i] = dp[i - 1] + nums[i]
    } else {
      dp[i] = nums[i]
    }
  }
  return Math.max.apply(null, dp)
};

console.log(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
console.log(maxSubArray([-2, -1]));
