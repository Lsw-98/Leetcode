// 统计一个数字在排序数组中出现的次数。

// 示例 1:
// 输入: nums = [5,7,7,8,8,10], target = 8
// 输出: 2

// 示例 2:
// 输入: nums = [5,7,7,8,8,10], target = 6
// 输出: 0


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  ans = 0
  for (let i of nums) {
    if (i === target) {
      ans += 1
    }
  }
  return ans
};