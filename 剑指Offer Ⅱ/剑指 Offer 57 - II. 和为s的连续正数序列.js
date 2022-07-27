/**
 * @param {number} target
 * @return {number[][]}
 */
var findContinuousSequence = function (target) {
  const res = []
  let left = 1
  let right = left + 1
  let nums = [left, right]
  let add = left + right
  while (left <= target) {
    if (nums.length >= 2 && add === target) {
      res.push(JSON.parse(JSON.stringify(nums)))
      left += 1
      right = left + 1
      nums = [left, right]
      add = left + right
    } else if (add < target) {
      right += 1
      nums.push(right)
      add += right
    } else {
      left += 1
      right = left + 1
      nums = [left, right]
      add = left + right
    }
  }
  return res
};

console.log(findContinuousSequence(15));
