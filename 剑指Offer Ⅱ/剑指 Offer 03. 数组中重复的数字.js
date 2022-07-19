var findRepeatNumber = function (nums) {
  // 先排序，再判断
  // nums.sort((a, b) => { return a - b })

  // for (let i = 1; i < nums.length; i++) {
  //   if (nums[i] === nums[i - 1]) return nums[i]
  // }
  // return 

  // Map
  const m = new Map()
  for (let i = 0; i < nums.length; i++) {
    if (m.has(nums[i])) {
      return nums[i]
    }else{
      m.set(nums[i], 1)
    }
  }
};

console.log(findRepeatNumber([2, 3, 1, 0, 2, 5, 3]));