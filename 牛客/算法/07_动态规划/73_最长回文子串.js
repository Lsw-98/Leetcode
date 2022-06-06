/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param A string字符串 
 * @return int整型
 */
function getLongestPalindrome(A) {
  const dp = new Array(A.length).fill(0).map(i => {
    return new Array(A.length).fill(0)
  })

  let res = 0

  for (let i = 0; i < dp.length; i++) {
    let temp = []
    for (let j = i; j < dp[i].length; j++) {
      temp.push(A[j])
      const tempReverse = JSON.parse(JSON.stringify(temp.reverse()))
      temp.reverse()
      if (tempReverse.join("") === temp.join("")) {
        dp[i][j] = temp.length
      }
    }
    if (res < Math.max(...dp[i])) {
      res = Math.max(...dp[i])
    }
  }
  return res
}
module.exports = {
  getLongestPalindrome: getLongestPalindrome
};

console.log(getLongestPalindrome("ababc"));