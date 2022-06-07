/**
 * @param {number[]} nums
 * @return {number}
 */
var wiggleMaxLength = function (nums) {
  if (nums.length === 1) {
    return 1
  }
  let currdiff = 0 // 当前的差值
  let prediff = 0 // 前一对差值
  let result = 1 // 峰值个数
  for (let i = 0; i < nums.length - 1; i++) {
    currdiff = nums[i + 1] - nums[i]
    if ((currdiff > 0 && prediff <= 0) || (prediff >= 0 && currdiff < 0)) {
      result += 1
      prediff = currdiff
    }
  }
  return result
};


console.log(wiggleMaxLength([1, 7, 4, 9, 2, 5]));
console.log(wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]));
console.log(wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]));
console.log(wiggleMaxLength([0, 0]));
