/**
 * @param {number} n
 * @return {number}
 */
var cuttingRope = function (n) {
  // 1. 我们想要求长度为n的绳子剪掉后的最大乘积，可以从前面比n小的绳子转移而来
  // 2. 用一个dp数组记录从0到n长度的绳子剪掉后的最大乘积，也就是dp[i]表示长度为i的绳子剪成m段后的最大乘积，初始化dp[2] = 1
  // 3. 我们先把绳子剪掉第一段（长度为j），如果只剪掉长度为1，对最后的乘积无任何增益，所以从长度为2开始剪
  // 4. 剪了第一段后，剩下(i - j)长度可以剪也可以不剪。如果不剪的话长度乘积即为j * (i - j)；如果剪的话长度乘积即为j * dp[i - j]。取两者最大值max(j * (i - j), j * dp[i - j])
  // 5. 第一段长度j可以取的区间为[2, i)，对所有j不同的情况取最大值，因此最终dp[i]的转移方程为dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
  // 6. 最后返回dp[n]即可
  const dp = new Array(n + 1).fill(1)
  for (let i = 3; i < n + 1; i++) {
    for (let j = 2; j < i; j++) {
      dp[i] = Math.max(dp[i], Math.max((j * (i - j)), (j * dp[i - j])))
    }
  }
  return dp[n]
};

console.log(cuttingRope(120));
