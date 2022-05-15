// 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
// 两个相邻元素间的距离为 1 。

// 示例 1：
// 输入：mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
// 输出：[[0, 0, 0], [0, 1, 0], [0, 0, 0]]

// 示例 2：
// 输入：mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
// 输出：[[0, 0, 0], [0, 1, 0], [1, 2, 1]]


/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var updateMatrix = function (mat) {
  let m = mat.length,
    n = mat[0].length;

  // 目标结果
  let dist = new Array(m).fill(0).map(() => new Array(n).fill(Number.MAX_SAFE_INTEGER));

  // 如果 (i, j) 的元素为 0，那么距离为 0
  for (let i = 0; i < m; i++)
    for (let j = 0; j < n; j++)
      if (mat[i][j] == 0)
        dist[i][j] = 0;

  // 只有 水平向右移动 和 竖直向下移动，递归的顺序是从左到右，从上到下
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      // 水平向左 是由同行左侧的元素递推算出来的
      if (i - 1 >= 0) dist[i][j] = Math.min(dist[i][j], dist[i - 1][j] + 1);
      // 垂直向下，是由同列上行的元素递推算出来的
      if (j - 1 >= 0) dist[i][j] = Math.min(dist[i][j], dist[i][j - 1] + 1);
    }
  }
  // 只有 水平向左移动 和 竖直向上移动，递归的顺序是从右到左，从下到上
  for (let i = m - 1; i >= 0; i--) {
    for (let j = n - 1; j >= 0; j--) {
      // 水平向右 是由同行右侧的元素递推算出来的
      if (i + 1 < m) dist[i][j] = Math.min(dist[i][j], dist[i + 1][j] + 1);
      // 垂直向下，是由同列下行的元素递推算出来的
      if (j + 1 < n) dist[i][j] = Math.min(dist[i][j], dist[i][j + 1] + 1);
    }
  }
  return dist;
};


console.log(updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]));
console.log(updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]));