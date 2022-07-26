/**
 * @param {string} s
 * @return {character}
 */
var firstUniqChar = function (s) {
  const keys = []
  const values = []

  for (let i = 0; i < s.length; i++) {
    if (keys.includes(s[i])) {
      values[keys.indexOf(s[i])] += 1
    } else {
      keys.push(s[i])
      values.push(1)
    }
  }
  for (let i = 0; i < values.length; i++) {
    if (values[i] === 1) {
      return keys[i]
    }
  }
  return " "
};

console.log(firstUniqChar("abaccdeff"));
