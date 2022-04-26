// 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

// 示例 1：
// 输入：n = 3
// 输出：5

// 示例 2：
// 输入：n = 1
// 输出：1


/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function (n) {
  // f(n) = f(n-1) + f(n-2)*f(1) + … + f(1)*f(n-2) + f(n-1);
  if (n === 0) return 0
  if (n === 1) return 1

  const dp = [1, 1]

  for (let i = 2; i < n; i++) {
    let num = 0
    for (let j = 0; j < i; j++) {
      num += dp[j] * dp[i - j - 1]
    }
    dp.push(num)
  }

  return dp[dp.length - 1]
};


console.log(numTrees(3));
console.log(numTrees(1));
