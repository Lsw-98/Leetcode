/**
 * @param {number[]} nums
 * @return {string}
 */
var minNumber = function (nums) {
  function isBiger(a, b) {
    return a + b > b + a ? true : false
  }

  nums.sort()

  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (isBiger(String(nums[i]), String(nums[j]))) {
        const temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
      }
    }
  }

  return nums.join("")
};

console.log(minNumber([10, 2]));
console.log(minNumber([3, 30, 34, 5, 9]));
