"""

给定一个m x n 二维字符网格board 和一个字符串单词word 。如果word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true

示例 3
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false

"""


def exist(board, word):
    n = len(board)
    m = len(board[0])
    word = list(word)
    fangxiang = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def dfs(x, y, index):
        if index == len(word):
            return True
        for k in range(len(fangxiang)):
            if 0 <= x + fangxiang[k][0] < n and 0 <= y + + fangxiang[k][1] < m and board[x + fangxiang[k][0]][y + fangxiang[k][1]] == word[index]:
                temp = board[x][y]
                board[x][y] = '#'
                if dfs(x + fangxiang[k][0], y + fangxiang[k][1], index + 1):
                    return True
                board[x][y] = temp
        return False

    for i in range(n):
        for j in range(m):
            if word[0] == board[i][j]:
                if dfs(i, j, 1):
                    return True
    return False


print(exist([["C","A","A"],["A","A","A"],["B","C","D"]], 'AAB'))
print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCCED'))
print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'SEE'))
print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCB'))
