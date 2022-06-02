/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param nums int整型一维数组 
 * @return int整型
 */
function minNumberDisappeared(nums) {
  nums = [...new Set(nums)]

  nums.sort((a, b) => {
    return a - b
  })

  let index = 0

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] <= 0) {
      continue
    }
    index = i
    break
  }

  if (nums[index] !== 1) {
    return 1
  }

  for (let i = index; i < nums.length - 1; i++) {
    if (nums[i + 1] - nums[i] !== 1) {
      return nums[i] + 1
    }
  }
  return nums[nums.length - 1] + 1
}
module.exports = {
  minNumberDisappeared: minNumberDisappeared
};
