// 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
//

// 示例 1：
// 输入：board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
// 输出：[["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
// 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
// 如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

// 示例 2：
// 输入：board = [["X"]]
// 输出：[["X"]]


/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function (board) {

  function dfs(board, r, c) {
    if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] === "V") {
      return
    }

    if (board[r][c] === "X") {
      return
    }

    board[r][c] = "V"

    dfs(board, r - 1, c)
    dfs(board, r + 1, c)
    dfs(board, r, c - 1)
    dfs(board, r, c + 1)
  }

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if ((i === 0 || i === board.length - 1 || j === 0 || j === board[0].length - 1) && board[i][j] === "O") {
        dfs(board, i, j)
      }
    }
  }

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j] === "O") {
        board[i][j] = "X"
      }
      if (board[i][j] === "V") {
        board[i][j] = "O"
      }
    }
  }
  console.log(board);
};


console.log(solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]));
console.log(solve([["X"]]));
console.log(solve([["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]));
