/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  const m = []
  let res = 0
  for (let i = 0; i < s.length; i++) {
    if (m.includes(s[i])) {
      const index = m.indexOf(s[i]) + 1
      for (let j = 0; j < index; j++) {
        m.shift()
      }
      m.push(s[i])
    } else m.push(s[i])
    if (res < m.length) res = m.length
  }
  return res
};

console.log(lengthOfLongestSubstring("ohvhjdml"));
