/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param nums int整型一维数组 
 * @return int整型
 */
function findPeakElement(nums) {
  let left = 1
  let right = nums.length - 2

  while (left <= right) {
    if (nums[left - 1] < nums[left] && nums[left] > nums[left + 1]) {
      return left
    }
    if (nums[right - 1] < nums[right] && nums[right] > nums[right + 1]) {
      return right
    }
    left += 1
    right -= 1
  }
  return nums.indexOf(Math.max(...nums))
}
module.exports = {
  findPeakElement: findPeakElement
};

console.log(findPeakElement([3, 6]));