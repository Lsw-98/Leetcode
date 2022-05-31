/**
 * 
 * @param A int整型一维数组 
 * @param B int整型一维数组 
 * @return void
 */
function merge(A, m, B, n) {
  let i = 0
  let j = 0

  while (i < A.length && j < B.length) {
    if (A[i] < B[j]) {
      i += 1
    } else if (A[i] > B[j]) {
      A.splice(i, 0, B[j])
      i += 1
      j += 1
    } else {
      A.splice(i, 0, B[j])
      i += 1
      j += 1
    }
  }

  while (j < n) {
    A.splice(A.length, 0, B[j])
    j += 1
  }
  return A
}
module.exports = {
  merge: merge
};


console.log(merge([4, 5, 6], 3, [1, 2, 3], 3));
console.log(merge([1, 2, 3], 3, [2, 5, 6], 3));
console.log(merge([4], 1, [1, 2, 3, 5, 6], 5));
