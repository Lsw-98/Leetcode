/**
 * longest common substring
 * @param str1 string字符串 the string
 * @param str2 string字符串 the string
 * @return string字符串
 */
function LCS(str1, str2) {
  if (str1.length === 0 || str2.length === 0) {
    return -1
  }

  let dp = new Array(str1.length).fill('').map(() => {
    return Array(str2.length).fill('')
  });
  let res = ""

  for (let i = 0; i < dp.length; i++) {
    for (let j = 0; j < dp[i].length; j++) {
      if (i === 0 || j === 0) {
        if (str1[i] === str2[j]) {
          dp[i][j] = str1[i]
        }
      } else {
        if (str1[i] === str2[j]) {
          dp[i][j] = dp[i - 1][j - 1] + str1[i]
        }
      }
      if (res.length < dp[i][j].length) {
        res = dp[i][j]
      }
    }
  }

  return res
}
module.exports = {
  LCS: LCS
};


console.log(LCS("1AB2345CD", "12345EF"));