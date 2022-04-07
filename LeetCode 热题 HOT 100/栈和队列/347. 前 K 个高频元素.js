/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  obj = {}
  for (let i in nums) {
    if (obj.hasOwnProperty(nums[i])) {
      obj[nums[i]] += 1
    } else {
      obj[nums[i]] = 1
    }
  }
  const sorted_keys_array = Object.keys(obj).sort((a, b) => {
    return obj[b] - obj[a];
  })
  res = []
  for (let index = 0; index < k; index++) {
    res.push(parseInt(sorted_keys_array[index]))
  }
  return res
}


console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2));
console.log(topKFrequent([1], 1));
