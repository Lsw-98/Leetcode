/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function (s, t) {
  const m = s.split("")
  for (let i = 0; i < t.length; i++) {
    if (m.includes(t[i])) m[m.indexOf(t[i])] = ""
    else return t[i]
  }
};

console.log(findTheDifference("a", "aa"));