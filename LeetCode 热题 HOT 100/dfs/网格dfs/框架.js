/**
 * 
 * @param {*} grid ：二维数组
 * @param {*} r ：行坐标
 * @param {*} c ：列坐标
 */
function dfs(grid, r, c) {
  // 判断base case
  // 如果坐标(r, c)超出了网格范围，直接返回
  if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] === "0") {
    return
  }


  // 如果这个格子不是岛屿，直接返回
  if (grid[r][c] != 1) {
    return
  }

  // 将格子标记为已遍历过
  grid[r][c] = 2

  // 访问上下左右四个相邻节点
  dfs(grid, r - 1, c)
  dfs(grid, r + 1, c)
  dfs(grid, r, c - 1)
  dfs(grid, r, c + 1)

}
