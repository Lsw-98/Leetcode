/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  const m = new Map()
  for (let i = 0; i < nums.length; i++) {
    if (m.has(nums[i])) {
      m.set(nums[i], m.get(nums[i]) + 1)
    } else {
      m.set(nums[i], 1)
    }
  }
  return m.get(target) ? m.get(target): 0
};