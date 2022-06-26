/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param A string字符串 
 * @return int整型
 */
function getLongestPalindrome(A) {
  const dp = new Array(A.length).fill(0).map(() => {
    return new Array(A.length).fill(0)
  })

  let res = 0

  for (let i = 0; i < dp.length; i++) {
    for (let j = 0; j < dp[0].length; j++) {
      if (A[i] === A[A.length - j - 1]) {
        if (i === 0 || j === 0) {
          dp[i][j] = 1
        } else {
          dp[i][j] = dp[i - 1][j - 1] + 1
        }
      }
      if (res < dp[i][j]) {
        res = dp[i][j]
      }
    }
  }
  return res
}
module.exports = {
  getLongestPalindrome: getLongestPalindrome
};

// 这个通过不了
console.log(getLongestPalindrome("acbdcbbbdbdaaccbcacdacdccababcddabddaaaaaaabdbabcdddaacabacbacbbdabdacddbbadaacbbdcbccacacdabcabacacbbbdcccacdcdcdcbcbabdcdacdddbbabcaccddddddabdacaabccdcabcbcbabacaaaccaccaddabbdadcdacdcdbaadbcabdcdcaaacbcadccbbddbaddcaddcaadcbbcbbdcbdadcddabdddcdbddbbdabaaddcaadd"));