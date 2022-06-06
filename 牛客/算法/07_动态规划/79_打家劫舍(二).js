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

  const dp1 = new Array(nums.length + 1).fill(0)
  const dp2 = new Array(nums.length + 1).fill(0)
  for (let i = 2; i < dp1.length; i++) {
    dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + nums[i - 2])
  }
  for (let i = 2; i < dp2.length; i++) {
    dp2[i] = Math.max(dp2[i - 1], dp2[i - 2] + nums[i - 1])
  }
  return Math.max(dp1[dp1.length - 1], dp2[dp2.length - 1])
}
module.exports = {
  rob: rob
};
