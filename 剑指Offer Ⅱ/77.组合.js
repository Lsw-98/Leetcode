/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function (n, k) {
  const res = []
  const temp = []
  const arr = new Array(n).fill(1).map((item, index) => index + 1)

  function backtrace(index) {
    if (temp.length === k) {
      res.push(JSON.parse(JSON.stringify(temp)))
      return
    }

    for (let i = index; i < arr.length; i++) {
      temp.push(arr[i])
      backtrace(i + 1)
      temp.pop()
    }
  }

  backtrace(0)
  return res
};

console.log(combine(4, 2));