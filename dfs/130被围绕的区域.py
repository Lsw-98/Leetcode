"""

给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的'O' 用 'X' 填充

示例 1：
输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的'O'都不会被填充为'X'
任何不在边界上，或不与边界上的'O'相连的'O'最终都会被填充为'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

示例 2：
输入：board = [["X"]]
输出：[["X"]]

"""


def solve(board):
    n = len(board)
    m = len(board[0])

    def dfs(x, y):
        board[x][y] = 'Z'
        if x - 1 > 0:
            if board[x - 1][y] == 'O':
                dfs(x - 1, y)
        if x + 1 < n + 2:
            if board[x + 1][y] == 'O':
                dfs(x + 1, y)
        if y - 1 > 0:
            if board[x][y - 1] == 'O':
                dfs(x, y - 1)
        if y + 1 < m + 2:
            if board[x][y + 1] == 'O':
                dfs(x, y + 1)

    board.insert(0, ['O' for _ in range(m + 2)])
    for i in range(1, n + 1):
        board[i].append('O')
        board[i].insert(0, 'O')
    board.append(['O' for _ in range(m + 2)])

    dfs(0, 0)

    for j in range(n + 2):
        for k in range(m + 2):
            if board[j][k] == 'Z':
                board[j][k] = 'O'
            elif board[j][k] == 'O':
                board[j][k] = 'X'

    del board[0]
    del board[-1]
    for i in range(n):
        del board[i][0]
        del board[i][-1]
    return board


print(solve([["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]]))
print(solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
