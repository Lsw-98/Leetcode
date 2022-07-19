/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function (n) {
  // 超时
  // const res = [1]
  // if (n === 1) {
  //   return res[0]
  // } else {
  //   for (let i = 2; ; i++) {
  //     if (res.length >= n) break
  //     let temp = i
  //     while (temp % 5 === 0) {
  //       temp /= 5
  //     }
  //     while (temp % 3 === 0) {
  //       temp /= 3
  //     }
  //     while (temp % 2 === 0) {
  //       temp /= 2
  //     }
  //     if (temp === 1) {
  //       res.push(i)
  //     }
  //   }
  // }

  // return res[res.length - 1]

  // dp
  const dp = [1]
  let a = 0
  let b = 0
  let c = 0
  for (let i = 1; i < n; i++) {
    dp[i] = Math.min(dp[a] * 2, dp[b] * 3, dp[c] * 5)
    if (dp[i] === dp[a] * 2) {
      a += 1
    }
    if (dp[i] === dp[b] * 3) {
      b += 1
    }
    if (dp[i] === dp[c] * 5) {
      c += 1
    }
  }
  return dp[dp.length - 1]
};

console.log(nthUglyNumber(10));