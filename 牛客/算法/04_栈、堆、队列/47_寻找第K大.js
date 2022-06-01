/**
 * 
 * @param a int整型一维数组 
 * @param n int整型 
 * @param K int整型 
 * @return int整型
 */
function findKth(a, n, K) {
  if (K === 0 || a.length === 0) {
    return []
  }

  a.sort(function (a, b) {
    return b - a
  })

  return a[K - 1]
}
module.exports = {
  findKth: findKth
};