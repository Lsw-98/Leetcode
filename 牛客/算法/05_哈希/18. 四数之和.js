/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function (nums, target) {
  const res = []
  if (nums.length < 4) return res
  nums.sort((a, b) => {
    return a - b
  })

  for (let i = 0; i < nums.length; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) {
      continue
    }
    for (let j = i + 1; j < nums.length; j++) {
      if (j > i + 1 && nums[j] === nums[j - 1]) {
        continue
      }
      let left = j + 1
      let right = nums.length - 1
      while (left < right) {
        if (left > j + 1 && nums[left] === nums[left - 1]) {
          left += 1
          continue
        }
        if (nums[i] + nums[j] + nums[left] + nums[right] === target) {
          res.push([nums[i], nums[j], nums[left], nums[right]])
          left += 1
          right -= 1
        } else if (nums[i] + nums[j] + nums[left] + nums[right] > target) {
          right -= 1
        } else {
          left += 1
        }
      }
    }
  }
  return res
};


console.log(fourSum([-2, -1, -1, 1, 1, 2, 2], 0));
console.log(fourSum([2, 2, 2, 2, 2], 8));
