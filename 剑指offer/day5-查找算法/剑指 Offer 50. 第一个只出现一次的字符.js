// 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

// 示例 1:
// 输入：s = "abaccdeff"
// 输出：'b'

// 示例 2:
// 输入：s = ""
// 输出：' '


/**
 * @param {string} s
 * @return {character}
 */
var firstUniqChar = function (s) {
  const obj = {}
  for (let i = 0; i < s.length; i++) {
    const key = s[i]
    if (obj[key]) {
      obj[key] += 1
    } else {
      obj[key] = 1
    }
  }

  for (let item in obj) {
    if (obj[item] === 1) {
      return item
    }
  }
  return " "
};


console.log(firstUniqChar("abaccdeff"));
console.log(firstUniqChar(""));

