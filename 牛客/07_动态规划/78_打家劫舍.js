/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param nums int整型一维数组 
 * @return int整型
 */
function rob(nums) {
  if (nums.length === 1) {
    return nums[0]
  }

  const dp = new Array(nums.length).fill(0)
  dp[0] = nums[0]
  dp[1] = nums[1]

  for (let i = 2; i < nums.length; i++) {
    dp[i] = dp[i - 2] + nums[i]
  }
  return Math.max(...dp)
}
module.exports = {
  rob: rob
};

console.log(rob([1, 2, 3, 4]));
console.log(rob([1, 3, 6]));
console.log(rob([2, 10, 5]));
