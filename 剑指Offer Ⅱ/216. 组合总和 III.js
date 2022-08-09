/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function (k, n) {
  const res = []
  const temp = 0

  function backtrace(index) {
    if (temp === n) {
      res.push(JSON.parse(JSON.stringify(temp)))
      return
    }

    for (let i = index; i < 9; i++) {
      temp += arr[i]
      backtrace(i + 1)
      temp -= arr[i]
    }
  }

  backtrace(0)
  return res
};