/**
 * @param {string} s
 * @return {string[]}
 */
var permutation = function (s) {
  const res = []
  if (s === "") return res
  let temp = []
  let used = new Array(s.length).fill(0)

  function backtrace(index) {
    if (temp.length === 3) {
      res.push(temp.join(""))
      return
    }

    for (let i = 0; i < s.length; i++) {
      if (used[i] === 1) {
        continue
      }
      used[i] = 1
      temp.push(s[i])
      backtrace(index)
      temp.pop()
      used[i] = 0
    }
  }

  backtrace(0)
  return res
};

console.log(permutation("aab"));
console.log(permutation("abc"));
