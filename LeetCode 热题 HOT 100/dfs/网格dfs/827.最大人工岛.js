// 给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。
// 返回执行此操作后，grid 中最大的岛屿面积是多少？
// 岛屿 由一组上、下、左、右四个方向相连的 1 形成。

// 示例 1:
// 输入: grid = [[1, 0], [0, 1]]
// 输出: 3
// 解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。

// 示例 2:
// 输入: grid = [[1, 1], [1, 0]]
// 输出: 4
// 解释: 将一格0变成1，岛屿的面积扩大为 4。

// 示例 3:
// 输入: grid = [[1, 1], [1, 1]]
// 输出: 4
// 解释: 没有0可以让我们变成1，面积依然为 4。



/**
 * @param {number[][]} grid
 * @return {number}
 */
var largestIsland = function (grid) {
  // 对于每个0，先把它赋值为1，超时
  // let maxArea = 0
  // let tempArea = 0

  // function dfs(grid, r, c) {
  //   if (0 > r || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] === 0) {
  //     return
  //   }

  //   grid[r][c] = 0
  //   tempArea += 1
  //   if (maxArea < tempArea) {
  //     maxArea = tempArea
  //   }

  //   dfs(grid, r - 1, c)
  //   dfs(grid, r + 1, c)
  //   dfs(grid, r, c + 1)
  //   dfs(grid, r, c - 1)
  // }

  // for (let i = 0; i < grid.length; i++) {
  //   for (let j = 0; j < grid[0].length; j++) {
  //     if (grid[i][j] === 0) {
  //       grid[i][j] = 1
  //       let temoGrid = JSON.parse(JSON.stringify(grid))
  //       dfs(temoGrid, i, j)
  //       grid[i][j] = 0
  //       tempArea = 0
  //     }
  //   }
  // }

  // if (maxArea) {
  //   return maxArea
  // } else {
  //   return grid.length * grid[0].length
  // }
};


console.log(largestIsland([[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0, 0]]));
console.log(largestIsland([[1, 1], [1, 0]]));
console.log(largestIsland([[1, 1], [1, 1]]));
