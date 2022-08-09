/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var add = function (a, b) {
  while (b != 0) {
    let sum = 0;
    let carry = 0;
    sum = a ^ b
    carry = (a & b) << 1
    a = sum
    b = carry
  }

  return a
};