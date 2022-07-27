/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  const arr = new Array(nums.length + 1).fill(1).map((item, index) => {
    return index
  })
  console.log(arr);
  for (let i = 0; i < nums.length; i++) {
    if (arr[i] !== nums[i]) {
      return arr[i]
    }
  }
  return arr[arr.length - 1]
};