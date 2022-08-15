/**
 * @param {number[]} a
 * @return {number[]}
 */
var constructArr = function (a) {
  let temp = 1;
  const res = new Array(a.length).fill(1)

  for (let i = 1; i < a.length; i++) {
    res[i] = res[i - 1] * a[i - 1]
  }

  for (let i = a.length - 2; i >= 0; i--) {
    temp *= a[i + 1]
    res[i] *= temp
  }
  return res
};

console.log(constructArr([1, 2, 3, 4, 5]));