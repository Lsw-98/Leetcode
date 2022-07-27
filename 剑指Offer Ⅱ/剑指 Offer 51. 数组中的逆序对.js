/**
 * @param {number[]} nums
 * @return {number}
 */
var reversePairs = function (nums) {
  let res = 0
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[j] < nums[i]) {
        res += 1
      }
    }
  }
  return res
};
