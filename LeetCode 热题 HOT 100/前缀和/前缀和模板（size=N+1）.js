function preFix(nums) {
  let sum = []
  sum[0] = nums[0]
  for (let i = 0; i < nums.length; i++) {
    sum[i + 1] = sum[i] + nums[i]
  }
}
