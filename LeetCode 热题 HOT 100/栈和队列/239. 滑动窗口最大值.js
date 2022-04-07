/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function (nums, k) {
  let queue = []
  let res = []

  for (let i = 0; i < k; i++) {
    queue.push(nums[i])
  }
  maxNum = Math.max.apply(null, queue)
  res.push(maxNum)

  for (let j = k; j < nums.length; j++) {
    const temp = queue.shift()
    queue.push(nums[j])
    if (temp !== maxNum && queue[queue.length - 1] < maxNum) {
      res.push(maxNum)
    } else {
      maxNum = Math.max.apply(null, queue)
      res.push(maxNum)
    }
  }
  return res
};


console.log(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3));
console.log(maxSlidingWindow([1], 1));
