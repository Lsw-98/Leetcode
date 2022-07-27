/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function (nums, k) {
  if (k === 0) return []
  const res = []
  for (let i = 0; i <= nums.length - k; i++) {
    let maxNum = -Infinity
    for (let j = 0; j < k; j++) {
      if (maxNum < nums[i + j]) maxNum = nums[i + j]
    }
    res.push(maxNum)
  }
  return res
};

console.log(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3));