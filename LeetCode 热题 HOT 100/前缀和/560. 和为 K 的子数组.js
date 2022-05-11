// 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

// 示例 1：
// 输入：nums = [1, 1, 1], k = 2
// 输出：2

// 示例 2：
// 输入：nums = [1, 2, 3], k = 3
// 输出：2


/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function (nums, k) {
  // 超时
  // let count = 0
  // let sum = []
  // sum[0] = 0
  // for (let i = 1; i <= nums.length; i++) {
  //   sum[i] = sum[i - 1] + nums[i - 1]
  // }

  // for (let i = 0; i < nums.length; i++) {
  //   for (let j = i + 1; j <= nums.length; j++) {
  //     if (sum[j] - sum[i] === k) {
  //       count += 1
  //     }
  //   }
  // }
  // return count

  
};


console.log(subarraySum([1, 1, 1], 2));
console.log(subarraySum([1, 2, 3], 3));
