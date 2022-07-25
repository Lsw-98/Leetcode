/**
 * @param {string} s
 * @return {string[]}
 */
var permutation = function (s) {
  const res = []
  if (s === "") return res
  let temp = ""
  function backtrace(index) {
    if (temp.length === 3) {
      res.push(temp)
      return
    }

    for (let i = 0; i < s.length; i++) {
      temp += s[i]
      backtrace(index + 1)
      temp -= s[i]
    }
  }

  backtrace(0)
  return res
};

console.log(permutation("abc"));
