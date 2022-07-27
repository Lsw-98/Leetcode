/**
 * @param {string} s
 * @param {number} n
 * @return {string}
 */
var reverseLeftWords = function (s, n) {
  tempLeft = s.slice(0, n)
  tempRight = s.slice(n)
  return tempRight + tempLeft
};