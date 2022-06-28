/**
 * longest common subsequence
 * @param s1 string字符串 the string
 * @param s2 string字符串 the string
 * @return string字符串
 */
function LCS(s1, s2) {
  if (s1 === '' || s2 === '') {
    return -1;
  }

  let dp = new Array(s1.length + 1).fill("").map(() => {
    return Array(s2.length + 1).fill("")
  });
  let m = s1.length;
  let n = s2.length;

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (s1[i - 1] === s2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + s1[i - 1];
      }
      else {
        dp[i][j] = dp[i - 1][j].length >= dp[i][j - 1].length ? dp[i - 1][j] : dp[i][j - 1];
      }
    }
  }

  return dp[m][n] == '' ? -1 : dp[m][n];
}
module.exports = {
  LCS: LCS
};


console.log(LCS("1A2C3D4B56", "B1D23A456A"));
console.log(LCS("1a1a31", "1a231"));
// console.log(LCS("abc", "abc"));
// console.log(LCS("ab", ""));
