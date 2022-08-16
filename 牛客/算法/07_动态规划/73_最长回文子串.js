/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param A string字符串 
 * @return int整型
 */
function getLongestPalindrome(A) {
  let res = 0
  const dp = new Array(A.length).fill(0).map(item => {
    return new Array(A.length).fill(0)
  })

  for (let c = 0; c <= A.length + 1; c++) {
    for (let i = 0; i < A.length - c; i++) {
      let j = c + i
      if (A[i] == A[j]) {
        if (c <= 1) {
          dp[i][j] = true
        } else {
          dp[i][j] = dp[i + 1][j - 1]
        }
      }
      if (dp[i][j]) {
        res = c + 1
      }
    }
  }

  return res
}


module.exports = {
  getLongestPalindrome: getLongestPalindrome
};

console.log(getLongestPalindrome("ccbcabaabba"));