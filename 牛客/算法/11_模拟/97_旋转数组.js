/**
 * 旋转数组
 * @param n int整型 数组长度
 * @param m int整型 右移距离
 * @param a int整型一维数组 给定数组
 * @return int整型一维数组
 */
function solve(n, m, a) {
  if (m > n) {
    m = m % n
  }
  const res = []
  for (let i = 0; i < n - m; i++) {
    res.push(a[i])
  }

  for (let i = n - 1; i >= n - m; i--) {
    res.unshift(a[i])
  }
  return res
}
module.exports = {
  solve: solve
};

console.log(solve(6, 7, [1, 2, 3, 4, 5, 6]));
console.log(solve(4, 0, [1, 2, 3, 4]));