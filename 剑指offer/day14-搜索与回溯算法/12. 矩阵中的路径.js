// 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
// 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
// 例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。


// 示例 1：
// 输入：board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word = "ABCCED"
// 输出：true

// 示例 2：
// 输入：board = [["a", "b"], ["c", "d"]], word = "abcd"
// 输出：false


/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {

  function dfs(i, j, index) {
    if (i >= board.length || i < 0 || j >= board[i].length || j < 0 || index >= word.length || board[i][j] !== word[index]) {
      return false
    } else if (index === word.length - 1) {
      return true
    } else {
      board[i][j] = "#"
      const result = dfs(i + 1, j, index + 1) ||
        dfs(i - 1, j, index + 1) ||
        dfs(i, j + 1, index + 1) ||
        dfs(i, j - 1, index + 1)
      board[i][j] = word[index]
      return result
    }
  }

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j] === word[0]) {
        if (dfs(i, j, 0)) return true
      }
    }
  }

  return false
};


console.log(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"));
console.log(exist([["a", "a"]], "aaa"));
console.log(exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"));
