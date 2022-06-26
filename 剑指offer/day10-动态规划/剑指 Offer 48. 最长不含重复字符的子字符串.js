/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let res = 0
  const temp = []
  for (let i = 0; i < s.length; i++) {
    if (temp.includes(s[i])) {
      const index = temp.indexOf(s[i]) + 1
      for (let i = 0; i < index; i++) {
        temp.shift()
      }
    }
    temp.push(s[i])
    if (res < temp.length) {
      res = temp.length
    }
  }
  return res
};

console.log(lengthOfLongestSubstring("abcabcbb"));
console.log(lengthOfLongestSubstring("bbbbb"));
console.log(lengthOfLongestSubstring("pwwkew"));