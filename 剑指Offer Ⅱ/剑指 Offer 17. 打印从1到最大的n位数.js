/**
 * @param {number} n
 * @return {number[]}
 */
var printNumbers = function (n) {
  let res = 0
  const num = 9
  let temp = 1
  for (let i = 0; i < n; i++) {
    res += num * temp
    temp *= 10
  }

  let result = []
  for (let i = 1; i <= res; i++) {
    result.push(i)
  }
  return result
};


console.log(printNumbers(3));
console.log(printNumbers(4));