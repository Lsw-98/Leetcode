/**
 * @param {number} n
 * @return {number[]}
 */
var printNumbers = function (n) {
  if (n === 0) return res
  let res = []
  const count = 9
  let temp = 0
  let multi = 1
  for (let i = 0; i < n; i++) {
    temp += count * multi
    multi *= 10
  }

  for (let i = 1; i <= temp; i++) {
    res.push(i)
  }
  return res
};

console.log(printNumbers(1));