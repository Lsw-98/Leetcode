/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function (n) {
  let res = 0
  while (n) {
    res += n & 1
    n >>= 1
  }
  return res
};

console.log(hammingWeight(11111111111111111111111111111101));