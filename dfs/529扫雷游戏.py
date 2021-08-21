"""

给定一个代表游戏板的二维字符矩阵。'M'代表一个未挖出的地雷，'E'代表一个未挖出的空方块，'B'代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，
数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X'则表示一个已挖出的地雷。

现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为'X'。
如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回面板。

示例 1：
输入:
[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
Click : [3,0]

输出:
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

示例 2：
输入:
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
Click : [1,2]

输出:
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

"""


def updateBoard(board, click):
    n = len(board)
    m = len(board[0])
    fangxiang = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    if board[click[0]][click[1]] == 'M':
        board[click[0]][click[1]] = 'X'
        return board

    def count(x, y):
        c = 0
        for i in range(len(fangxiang)):
            if 0 <= x + fangxiang[i][0] < n and 0 <= y + fangxiang[i][1] < m and board[x + fangxiang[i][0]][y + fangxiang[i][1]] == 'M':
                c += 1
        return c

    def dfs(x, y):
        num = count(x, y)
        if num:
            board[x][y] = str(num)
            return
        else:
            if board[x][y] == 'M':
                board[x][y] = 'X'
                return
            else:
                board[x][y] = 'B'
            for i in range(len(fangxiang)):
                if 0 <= x + fangxiang[i][0] < n and 0 <= y + fangxiang[i][1] < m and board[x + fangxiang[i][0]][y + fangxiang[i][1]] == 'E':
                    dfs(x + fangxiang[i][0], y + fangxiang[i][1])

    dfs(click[0], click[1])
    return board


print(updateBoard([["M","M","M","M","M","M"],["M","M","M","E","M","M"],["M","M","M","M","M","M"]], [1,2]))
print(updateBoard([['E', 'E', 'E', 'E', 'E'],  ['E', 'E', 'M', 'E', 'E'],  ['E', 'E', 'E', 'E', 'E'],  ['E', 'E', 'E', 'E', 'E']], [3, 0]))
print(updateBoard([['B', '1', 'E', '1', 'B'],  ['B', '1', 'M', '1', 'B'],  ['B', '1', '1', '1', 'B'],  ['B', 'B', 'B', 'B', 'B']], [1, 2]))
