// 给你一个大小为 m x n 的二进制矩阵 grid 。
// 岛屿 是由一些相邻的 1(代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。
// 你可以假设 grid 的四个边缘都被 0（代表水）包围着。
// 岛屿的面积是岛上值为 1 的单元格的数目。
// 计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

// 示例 1：
// 输入：grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
// [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
// [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
// 输出：6
// 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
// 示例 2：

// 输入：grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
// 输出：0


/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function (grid) {
  let maxArea = 0
  let tempArea = 0

  function dfs(grid, r, c) {
    if (0 > r || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] === 0) {
      return
    }

    grid[r][c] = 0
    tempArea += 1
    if (maxArea < tempArea) {
      maxArea = tempArea
    }

    dfs(grid, r - 1, c)
    dfs(grid, r + 1, c)
    dfs(grid, r, c + 1)
    dfs(grid, r, c - 1)
  }

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === 1) {
        dfs(grid, i, j)
        tempArea = 0
      }
    }
  }

  return maxArea
};


console.log(maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
[0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]));
console.log(maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]));
