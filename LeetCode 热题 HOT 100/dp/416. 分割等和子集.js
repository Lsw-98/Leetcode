// 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

// 示例 1：
// 输入：nums = [1, 5, 11, 5]
// 输出：true
// 解释：数组可以分割成[1, 5, 5] 和[11] 。

// 示例 2：
// 输入：nums = [1, 2, 3, 5]
// 输出：false
// 解释：数组不能分割成两个元素和相等的子集。


/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function (nums) {
  let dp = new Array(nums.length).fill(0).map(() => {
    return Array(nums.length).fill(0)
  });
  let sumNums = 0

  for (const iterator of nums) {
    sumNums += iterator
  }

  for (const i in dp) {
    dp[i][i] = nums[i]
    if (sumNums - dp[i][i] === sumNums / 2) {
      return true
    }
  }

  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < dp[i].length; j++) {
      if (dp[i][j - 1] + nums[j] <= sumNums / 2) {
        dp[i][j] = dp[i][j - 1] + nums[j]
        if (dp[i][j] === sumNums / 2) {
          return true
        }
      } else if (dp[i][j - 1] + nums[j] > sumNums / 2) {
        dp[i][j] = dp[i][j - 1]
      }
    }
  }
  return false
};


console.log(canPartition([14, 9, 8, 4, 3, 2]));
console.log(canPartition([1, 1]));
console.log(canPartition([1, 5, 11, 5]));
console.log(canPartition([1, 2, 3, 5]));
console.log(canPartition([1, 1, 2, 2]));
