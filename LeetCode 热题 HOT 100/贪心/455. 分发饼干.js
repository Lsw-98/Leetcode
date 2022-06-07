/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function (g, s) {
  let res = 0
  if (s.length === 0) {
    return res
  }

  g.sort((a, b) => {
    return a - b
  })
  s.sort((a, b) => {
    return a - b
  })
  let index = 0

  for (let i = 0; i < s.length; i++) {
    if (s[i] >= g[index]) {
      res += 1
      index += 1
    }
  }

  return res
};


// console.log(findContentChildren([1, 2, 3], [1, 1]));
// console.log(findContentChildren([1, 2], [1, 2, 3]));
console.log(findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]));
