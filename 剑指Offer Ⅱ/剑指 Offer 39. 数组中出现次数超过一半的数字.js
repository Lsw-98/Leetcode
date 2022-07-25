/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  const m = new Map()
  for (let i = 0; i < nums.length; i++) {
    if (m.has(nums[i])) {
      const temp = m.get(nums[i]) + 1
      m.set(nums[i], temp)
      if (m.get(nums[i]) >= nums.length / 2) {
        return nums[i]
      }
    } else {
      m.set(nums[i], 1)
    }
  }
  return nums[0]
};

console.log(majorityElement([1]));