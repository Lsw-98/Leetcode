/**
 * longest common subsequence
 * @param s1 string字符串 the string
 * @param s2 string字符串 the string
 * @return string字符串
 */
function LCS(s1, s2) {
  if (s1.length === 0 || s2.length === 0) {
    return -1
  }

  let dp = new Array(s1.length).fill(0).map(() => {
    return Array(s2.length).fill(0)
  });

  
  return -1
}
module.exports = {
  LCS: LCS
};


console.log(LCS("1A2C3D4B56", "B1D23A456A"));
console.log(LCS("abc", "def"));
console.log(LCS("abc", "abc"));
console.log(LCS("ab", ""));
