/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function (s) {
  let res = 0
  let flag = true

  const map = new Map()

  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i])) {
      map.set(s[i], map.get(s[i]) + 1)
    } else {
      map.set(s[i], 1)
    }
  }

  const arr = Array.from(map)
  arr.sort((a, b) => {
    return b[1] - a[1]
  })


  for (let i = 0; i < arr.length; i++) {
    if (arr[i][1] % 2 === 0) {
      res += arr[i][1]
    } else {
      if (flag) {
        res += arr[i][1]
        flag = false
      } else {
        const temp = arr[i][1] - 1
        res += temp
      }
    }
  }
  return res
};

console.log(longestPalindrome("abccccdd"));
console.log(longestPalindrome("a"));
console.log(longestPalindrome("bb"));
console.log(longestPalindrome("bananas"));
