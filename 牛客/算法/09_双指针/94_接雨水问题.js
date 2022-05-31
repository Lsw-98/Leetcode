/**
 * max water
 * @param arr int整型一维数组 the array
 * @return long长整型
 */
function maxWater(arr) {
  let res = 0
  if (arr.length < 3) {
    return res
  }

  let left = 0
  let right = 1
  while (right < arr.length) {
    if (arr[left] < arr[right]) {
      left += 1
      right += 1
    }
  }

  return res
}
module.exports = {
  maxWater: maxWater
};


console.log(maxWater([3, 1, 2, 5, 2, 4]));
console.log(maxWater([4, 5, 1, 3, 2]));
