/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  let maxIndex = 0
  for (let i = 0; i < nums.length; i++) {
    if (maxIndex >= i && maxIndex < i + nums[i]) {
      maxIndex = nums[i] + i
    }
  }

  return maxIndex >= nums.length - 1
};
