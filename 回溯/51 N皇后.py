"""

n皇后问题 研究的是如何将 n个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的n皇后问题 的解决方案。
每一种解法包含一个不同的n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例 1:
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

示例 2:
输入：n = 1
输出：[["Q"]]

"""


# 约束条件
# 不能同行
# 不能同列
# 不能同斜线

def solveNQueens(n):
    res = []
    s = '.' * n

    def backtrack(path=[], i=0, col_selected=[], z_diag=set(), f_diag=set()):
        if i == n:
            res.append(path)
            return
        for j in range(n):
            if j not in col_selected and i - j not in z_diag and i + j not in f_diag:
                backtrack(path + [s[:j] + 'Q' + s[j + 1:]], i + 1, col_selected + [j], z_diag | {i - j},
                          f_diag | {i + j})

    backtrack()
    return res


print(solveNQueens(4))
print(solveNQueens(1))
