function preFix(nums) {
  let sum = []
  sum[0] = nums[0]
  for (let i = 1; i < nums.length; i++) {
    sum[i] = sum[i - 1] + nums[i]
  }
}
